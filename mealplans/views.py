from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.template import loader
from django.contrib.auth.models import User
from .models import (
    Customer,
)
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
import json
from django.http import JsonResponse
from django.views import View
from datetime import datetime

# Create your views here.



def index(request):
    user = request.user

    context = {
        'user':request.user
    }
    return render(request,'home.html',context=context)



def signup(request):

    if request.user.is_authenticated:
        return redirect('/')  # Replace 'home' with the appropriate URL name or pat


    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create the User
        user = User.objects.create_user(
            username=email,  # or generate a unique username from email or another field
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        # Create the Customer
        customer = Customer.objects.create(user=user)
        
        # Log the user in and redirect to a success or home page
        login(request, user)
        return redirect('/')  # Replace 'home' with your actual redirect URL
    
    return render(request, 'auth/signup.html')


def login_view(request):

    
    if request.user.is_authenticated:
        return redirect('/')  # Replace 'home' with the appropriate URL name or pat

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('/')  # Change to your desired redirect URL
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'home.html')  # Redirect to base template to render popup





def logout_view(request):
    logout(request)
    return redirect('/')  # Change 'home' to your desired redirect URL after logout





# function for the BMI calculator
class BmiCalculatorView(View):
    template_name = 'bmi/calculator.html'

    def get(self, request):
        # Initialize variables for GET request
        return render(request, self.template_name, {
            'bmi': None,
            'errors': [],
            'form_data': {},
            'header': None,
            'review': None,
            'weight_range': None,
        })
    

    def post(self, request):
        bmi = None  # Initialize BMI variable
        error_messages = []  # Initialize error messages list
        form_data = {}  # Dictionary to hold form data for repopulation

        # Get form values
        form_data['gender'] = request.POST.get('gender')
        form_data['age'] = request.POST.get('age')
        form_data['height_feet'] = request.POST.get('height_feet')
        form_data['height_inch'] = request.POST.get('height_inch', 0)
        form_data['weight'] = request.POST.get("weight")

        # Validate fields and add error messages if any are missing
        if not form_data['gender']:
            error_messages.append("Gender is required.")
        if not form_data['age']:
            error_messages.append("Age is required.")
        if not form_data['height_feet']:
            error_messages.append("Height in feet is required.")
        if not form_data['weight']:
            error_messages.append("Weight is required.")

        # Calculate BMI only if there are no errors
        if not error_messages:
            try:
                # Convert height and weight to appropriate types
                height_feet = int(form_data['height_feet'])
                height_inch = int(form_data['height_inch'])
                weight = float(form_data['weight'])

                # Convert height to meters
                total_height_inch = (height_feet * 12) + height_inch
                height_meters = total_height_inch * 0.0254  # 1 inch = 0.0254 meters

                # Calculate BMI
                if height_meters > 0:
                    bmi = weight / (height_meters ** 2)

                    header, review = self.generate_bmi_review(bmi, form_data['gender'])
                    weight_range = self.generate_weight_range_message(height_meters, form_data['gender'], int(form_data['age']))

            except ValueError:
                error_messages.append("Please enter valid numeric values for height and weight.")

        # Render template with BMI, errors, and form data for repopulation
        return render(request, self.template_name, {
            'bmi': bmi,
            'errors': error_messages,
            'form_data': form_data,
            'header': header if bmi is not None else None,
            'review': review if bmi is not None else None,
            'weight_range': weight_range if bmi is not None else None,
        })
    
    def get_bmi_recommendations(self,age):
            """
            Get BMI recommendations based on age group.
            
            Args:
            age (int): Age of the individual.

            Returns:
            tuple: (lower BMI limit, upper BMI limit) for the age group.
            """
            if age < 18:  # Children and teens
                return (17.5, 24.0)  # Adjusted for younger individuals
            elif 18 <= age <= 24:  # Young adults
                return (18.5, 24.9)
            elif 25 <= age <= 64:  # Adults
                return (18.5, 24.9)
            else:  # Seniors
                return (18.0, 27.0)  # Slightly higher range for older adults

    def calculate_healthy_weight_range(self,height_meters, age):
            """
            Calculate the healthy weight range for a given height and age based on BMI values.
            
            Args:
            height_meters (float): Height in meters.
            age (int): Age of the individual.

            Returns:
            tuple: Lower and upper weight limits in kilograms.
            """
            # Get BMI limits based on age
            bmi_lower_limit, bmi_upper_limit = self.get_bmi_recommendations(age)

            # Calculate the weight range
            weight_lower = bmi_lower_limit * (height_meters ** 2)
            weight_upper = bmi_upper_limit * (height_meters ** 2)

            return round(weight_lower, 2), round(weight_upper, 2)

    def generate_weight_range_message(self,height_meters, gender, age):
            """
            Generate a message indicating the healthy weight range based on height, gender, and age.
            
            Args:
            height_meters (float): Height in meters.
            gender (str): Gender of the individual ('male' or 'female').
            age (int): Age of the individual.

            Returns:
            str: Message with the healthy weight range.
            """
            weight_range = self.calculate_healthy_weight_range(height_meters, age)
            weight_lower, weight_upper = weight_range
            height_meters = "{:.2f}".format(height_meters)

            if gender.lower() == 'male':
                return (f"For a male aged {age} years with a height of {height_meters} meters, "
                        f"the healthy weight range is approximately {weight_lower} kg to {weight_upper} kg.")
            elif gender.lower() == 'female':
                return (f"For a female aged {age} years with a height of {height_meters} meters, "
                        f"the healthy weight range is approximately {weight_lower} kg to {weight_upper} kg.")
            else:
                return (f"For an individual aged {age} years with a height of {height_meters} meters, "
                        f"the healthy weight range is approximately {weight_lower} kg to {weight_upper} kg.")


    def generate_bmi_review(self,bmi, gender='male'):
            """Generate a header and a review based on BMI value with contextual warnings."""
            
            if gender == 'female':
                if bmi < 18.5:
                    header = "Underweight"
                    if bmi <= 17:
                        review = (
                            "Your BMI is significantly below the healthy range. "
                            "It's critical to seek guidance to improve your nutritional intake."
                        )
                    elif 17 < bmi <= 18:
                        review = (
                            "Your BMI is low. Focus on consuming nutrient-dense foods to help increase your weight in a healthy manner."
                        )
                    else:  # 18 <= bmi < 18.5
                        review = (
                            "Your BMI is slightly below the healthy range. "
                            "Consider enhancing your diet with more calories from nutritious foods."
                        )

                elif 18.5 <= bmi < 19:
                    header = "Healthy Weight"
                    review = (
                        "You're in a healthy range for females. Maintaining a balanced diet and regular exercise is key."
                    )

                elif 19 <= bmi < 20:
                    header = "Healthy Weight"
                    review = (
                        "You're within a healthy BMI range. Keep up the good work with your diet and exercise!"
                    )

                elif 20 <= bmi < 22:
                    header = "Healthy Weight"
                    review = (
                        "Your BMI is good. Keep up your healthy eating habits and regular physical activity!"
                    )

                elif 22 <= bmi < 23:
                    header = "Healthy Weight"
                    review = (
                        "Your BMI is in a healthy range. Regular physical activity is important."
                    )

                elif 23 <= bmi < 25:
                    header = "Great Shape"
                    review = (
                        "You're well within the healthy BMI range. Ensure you keep a balanced diet and an active lifestyle."
                    )

                elif 25 <= bmi < 27:
                    header = "Overweight"
                    review = (
                        "Your BMI indicates you're slightly above the healthy range. Consider increasing your physical activity."
                    )

                elif 27 <= bmi < 29:
                    header = "Overweight"
                    review = (
                        "You're approaching the obesity range. Focus on healthier eating habits and regular exercise."
                    )

                else:  # bmi >= 29
                    if bmi < 35:
                        header = "Obesity"
                        review = (
                            "Your BMI indicates obesity. It's advisable to discuss your weight with a healthcare provider."
                        )
                    elif 35 <= bmi < 40:
                        header = "Moderate Obesity"
                        review = (
                            "Your BMI suggests serious weight concerns. Seeking support from a healthcare professional is important."
                        )
                    else:  # bmi >= 40
                        header = "Severe Obesity"
                        review = (
                            "Your BMI is significantly high. Immediate action and professional support are recommended for health management."
                        )

            else:  # For males
                if bmi < 18.5:
                    header = "Underweight"
                    if bmi <= 17:
                        review = (
                            "Your BMI is significantly below the healthy range. "
                            "It's critical to seek guidance to improve your nutritional intake."
                        )
                    elif 17 < bmi <= 18:
                        review = (
                            "Your BMI is low. Focus on consuming nutrient-dense foods to help increase your weight in a healthy manner."
                        )
                    else:  # 18 <= bmi < 18.5
                        review = (
                            "Your BMI is slightly below the healthy range. "
                            "Consider enhancing your diet with more calories from nutritious foods."
                        )

                elif 18.5 <= bmi < 20:
                    header = "Lightly Underweight"
                    review = (
                        "You're close to the healthy range. With some dietary adjustments, "
                        "you can reach a more balanced BMI."
                    )

                elif 20 <= bmi < 22:
                    header = "Near Healthy Weight"
                    review = (
                        "You're approaching a healthy BMI. Maintain a balanced diet and regular exercise "
                        "to stay in this range."
                    )

                elif 22 <= bmi < 24:
                    header = "Healthy Weight"
                    review = (
                        "Your BMI is good. Keep up your healthy eating habits and regular physical activity!"
                    )

                elif 24 <= bmi < 26:
                    header = "Healthy Weight"
                    review = (
                        "You are maintaining a healthy BMI. Continue your good habits to stay fit and active."
                    )

                elif 26 <= bmi < 28:
                    header = "Overweight"
                    review = (
                        "Your BMI indicates you're slightly above the healthy range. Consider increasing your physical activity."
                    )

                elif 28 <= bmi < 30:
                    header = "Overweight"
                    review = (
                        "You're approaching the obesity range. Focus on healthier eating habits and regular exercise."
                    )

                else:  # bmi >= 30
                    if bmi < 35:
                        header = "Obesity"
                        review = (
                            "Your BMI indicates obesity. It's advisable to discuss your weight with a healthcare provider."
                        )
                    elif 35 <= bmi < 40:
                        header = "Moderate Obesity"
                        review = (
                            "Your BMI suggests serious weight concerns. Seeking support from a healthcare professional is important."
                        )
                    else:  # bmi >= 40
                        header = "Severe Obesity"
                        review = (
                            "Your BMI is significantly high. Immediate action and professional support are recommended for health management."
                        )

            return header, review




class DashboardView(View):
    template_name = 'profile/dashboard.html'

    def generate_day_month_year(self):
         # Generate lists for days, months, and years
        days_list = list(range(1, 32))  # Days 1-31
        months_list = list(range(1, 13))  # Months 1-12
        current_year = datetime.now().year
        years_list = list(range(1900, current_year + 1))  # Years from 1900 to current year

        return {
            "days_list":days_list,
            "months_list":months_list,
            'years_list':years_list
        }

    def get(self,request):

        profile_data = get_object_or_404(Customer,user=request.user)

        dob_date = profile_data.dob
        
        dob = {
            'day': dob_date.day if dob_date else '',  # Extract day
            'month': dob_date.month if dob_date else '',  # Extract month
            'year': dob_date.year if dob_date else '',  # Extract year
        }

        # calling generate date month year function
        date_options = self.generate_day_month_year()

        representation = {
            'first_name': profile_data.user.first_name,
            'last_name': profile_data.user.last_name,
            'email':profile_data.user.email,
            'gender':profile_data.gender,
            'age':profile_data.age,
            'date_of_birth':profile_data.dob,
            'dob': dob,
            'height_feet':profile_data.height_feet,
            'height_inch':profile_data.height_inches
        }
        context = {
            'profile_data':representation,
            'date_options':date_options
        }
        return render(request,self.template_name,context)
    

    def post(self, request, *args, **kwargs):
          # Redirect to the dashboard or success page
          action = request.POST.get('action')
          
          print('action')
          if action == 'update_profile':
            #   print("updaing the profile")
              self.change_profile(request)

          return redirect('profile')
    

    def change_profile(self,request):
        customer = get_object_or_404(Customer, user=request.user)
        
        # Update Customer data
        customer.user.first_name = request.POST.get('first_name')
        customer.user.last_name = request.POST.get('last_name')
        customer.gender = request.POST.get('gender')

        # Process Date of Birth
        day = request.POST.get('day')
        month = request.POST.get('month')
        year = request.POST.get('year')
        if day and month and year:
            try:
                customer.dob = datetime(year=int(year), month=int(month), day=int(day))
            except ValueError:
                customer.dob = None  # Handle invalid date
        
        # Height in feet and inches
        customer.height_feet = request.POST.get('height_feet')
        customer.height_inches = request.POST.get('height_inch')
        
        # Save the updated data
        customer.user.save()
        customer.save()
        
        return redirect('profile')


def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        new_retype = request.POST.get('new_retype')

        user = request.user

        # Check if old password is correct
        if not user.check_password(old_password):
            messages.error(request, 'Old password is incorrect.')
            return render(request,'profile/dashboard.html')  # Replace 'profile' with your view name

        # Check if new passwords match
        if new_password != new_retype:
            messages.error(request, 'New passwords do not match.')
            return render(request,'profile/dashboard.html')  # Replace 'profile' with your view name


        # Update password
        user.set_password(new_password)
        user.save()

        # Keep the user logged in after password change
        update_session_auth_hash(request, user)

        messages.success(request, 'Your password has been successfully updated.')
        return render(request, 'profile/dashboard.html',{'password_success':True})  # Or the name of your main template

    return render(request, 'profile/dashboard.html')  # Or the name of your main template




    
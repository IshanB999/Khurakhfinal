from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Gender(models.TextChoices):
    MALE = 'male'
    FEMALE = 'female'
    OTHERS = 'others'


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.PositiveIntegerField(blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    height_feet = models.PositiveIntegerField("Height (feet)", blank=True, null=True)
    height_inches = models.PositiveIntegerField("Height (inches)", blank=True, null=True)
    gender = models.CharField(max_length=10,choices=Gender.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.email



class Mood(models.TextChoices):
    HAPPY = 'happy'
    NETURAL = 'netural'
    SAD = 'sad'

class BmiRange(models.Model):
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=20,choices=Gender.choices)
    top_bmi = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True)
    bottom_bmi = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    is_less_then_top = models.BooleanField(default=False)
    is_more_then_bottom = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.title


class ProgressReport(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    weight_kg = models.DecimalField("Weight (kg)", max_digits=5, decimal_places=2)
    mood = models.CharField(max_length=20,choices=Mood.choices)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    bmi_range= models.ForeignKey(BmiRange,on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)
    breakfast = models.TextField(help_text="Breakfast meal recommendation.",blank=True,null=True)
    lunch = models.TextField(help_text="Lunch meal recommendation.",blank=True,null=True)
    dinner = models.TextField(help_text="Dinner meal recommendation.",blank=True,null=True)
    snacks = models.TextField(help_text="Snack options for this meal plan.",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Food(models.Model):
    plan = models.ForeignKey(MealPlan,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title
    



class Blog(models.Model):
    header = models.CharField(max_length=100)
    banner_image = models.ImageField(upload_to='images/blog/',blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header
    

class BlogContents(models.Model):
    image = models.ImageField(upload_to='images/blog/content/',blank=True,null=True)
    header = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header
    
    def short_description(self):
        if self.description:
            words = self.description.split()
            if len(words) > 15:
                return ' '.join(words[:15]) + ' ...'
        return self.description



from django.db import models

class MealCategory(models.TextChoices):
    LOW_CARB = 'Low Carb', 'Low Carb'
    VEG = 'Vegetarian', 'Vegetarian'
    VEGAN = 'Vegan', 'Vegan'
    NON_VEG = 'Non-Vegetarian', 'Non-Vegetarian'

class Meal(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    calories = models.DecimalField(max_digits=6, decimal_places=2)  # Calories per serving
    protein = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    carbs = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    fats = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    category = models.CharField(max_length=20, choices=MealCategory.choices)
    image = models.ImageField(upload_to='meals/', blank=True, null=True)

    def __str__(self):
        return self.name

class PredefinedMealPlan(models.Model):
    category = models.CharField(max_length=20, choices=MealCategory.choices, unique=True)
    description = models.TextField(blank=True, null=True)  # Optional notes about the plan
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} Plan"

class PredefinedDailyMeal(models.Model):
    plan = models.ForeignKey(PredefinedMealPlan, on_delete=models.CASCADE, related_name='daily_meals')
    day = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])
    breakfast = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, related_name='default_breakfast_meals')
    lunch = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, related_name='default_lunch_meals')
    dinner = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, related_name='default_dinner_meals')
    snacks = models.ManyToManyField(Meal, related_name='default_snack_meals', blank=True)

    def __str__(self):
        return f"{self.plan.category} - {self.day}"

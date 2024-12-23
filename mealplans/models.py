from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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




# meal planner

class Plan(models.Model):
    title = models.CharField(max_length=200)
    header_text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/plan/',blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_popular = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title



class MealPlan(models.Model):
    title = models.CharField(max_length=200)
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE,related_name='meal_plans')
    image = models.ImageField(upload_to='images/plan/meal/',blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    is_popular = models.BooleanField(default=False)
    total_days = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MealPlanDescription(models.Model):
    plan = models.ForeignKey(MealPlan,on_delete=models.CASCADE,related_name='meal_plan_descriptions')
    header = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/plan/meal/description/',blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    list_item = models.JSONField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.header

class DayChoices(models.IntegerChoices):
    DAY1 = 1, 'Day 1'
    DAY2 = 2, 'Day 2'
    DAY3 = 3, 'Day 3'
    DAY4 = 4, 'Day 4'
    DAY5 = 5, 'Day 5'
    DAY6 = 6, 'Day 6'
    DAY7 = 7, 'Day 7'
    DAY8 = 8, 'Day 8'
    DAY9 = 9, 'Day 9'
    DAY10 = 10, 'Day 10'
    DAY11 = 11, 'Day 11'
    DAY12 = 12, 'Day 12'
    DAY13 = 13, 'Day 13'
    DAY14 = 14, 'Day 14'
    DAY15 = 15, 'Day 15'
    DAY16 = 16, 'Day 16'
    DAY17 = 17, 'Day 17'
    DAY18 = 18, 'Day 18'
    DAY19 = 19, 'Day 19'
    DAY20 = 20, 'Day 20'
    DAY21 = 21, 'Day 21'
    DAY22 = 22, 'Day 22'
    DAY23 = 23, 'Day 23'
    DAY24 = 24, 'Day 24'
    DAY25 = 25, 'Day 25'
    DAY26 = 26, 'Day 26'
    DAY27 = 27, 'Day 27'
    DAY28 = 28, 'Day 28'
    DAY29 = 29, 'Day 29'
    DAY30 = 30, 'Day 30'


class DailyPlan(models.Model):
    title = models.CharField(max_length=255)
    mealplan = models.ForeignKey(MealPlan,on_delete=models.CASCADE,related_name='daily_meals')
    day = models.IntegerField(choices=DayChoices.choices)
    image = models.ImageField(upload_to='images/plan/meal/',blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
            # Check if the current day is the next day in sequence
            if self.day != 1:
                previous_day_exists = DailyPlan.objects.filter(day=self.day - 1).exists()
                if not previous_day_exists:
                    raise ValidationError(f"You cannot create a meal for Day {self.day} until Day {self.day - 1} has been created.")

    def save(self, *args, **kwargs):
        # Call the clean method to validate
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class MealType(models.TextChoices):
    BREAKFAST = 'Breakfast', 'Breakfast'
    LUNCH = 'Lunch', 'Lunch'
    SNACKS = 'Snacks', 'Snacks'
    DINNER = 'Dinner', 'Dinner'

class FoodType(models.TextChoices):
    VEGAN = 'Vegan', 'Vegan'
    VEGETARIAN = 'Vegetarian', 'Vegetarian'
    NON_VEG = 'Non-Veg', 'Non-Veg'


class Meal(models.Model):
    daily_plan = models.ForeignKey(DailyPlan,on_delete=models.CASCADE,related_name='meals')
    meal_type = models.CharField(max_length=20, choices=MealType.choices)
    food_type = models.CharField(max_length=20, choices=FoodType.choices)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='images/plan/meal/',blank=True,null=True)
    food_list = models.JSONField(blank=True,null=True)
    calories = models.DecimalField(max_digits=6, decimal_places=2,blank=True,null=True)  # Calories per serving
    protein = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    carbs = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    fats = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def clean(self):
        # Ensure only one meal of each type and food type can be created per DailyPlan
        if Meal.objects.filter(daily_plan=self.daily_plan, meal_type=self.meal_type, food_type=self.food_type).exists():
            raise ValidationError(f"A {self.get_meal_type_display()} meal of {self.get_food_type_display()} type has already been created for Day {self.daily_plan.day}. You can only have one of each meal type and food type per day.")

    def save(self, *args, **kwargs):
        # Call the clean method to validate
        self.clean()
        super().save(*args, **kwargs)     
    def __str__(self):
            return f"{self.get_meal_type_display()} for Day {self.daily_plan.day} of {self.daily_plan.title}"
from django.contrib import admin

# Register your models here.


from . import models




class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'user_first_name', 'user_last_name', 'age', 'dob', 'gender', 'created_at')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')

    # Display related `User` fields in `CustomerAdmin`
    def user_email(self, obj):
        return obj.user.email

    def user_first_name(self, obj):
        return obj.user.first_name

    def user_last_name(self, obj):
        return obj.user.last_name

    # Define display names
    user_email.short_description = 'Email'
    user_first_name.short_description = 'First Name'
    user_last_name.short_description = 'Last Name'

# Register the admin class with the associated model
admin.site.register(models.Customer, CustomerAdmin)

# Admin configuration for BmiRange model
@admin.register(models.BmiRange)
class BmiRangeAdmin(admin.ModelAdmin):
    list_display = ('title', 'gender', 'top_bmi', 'bottom_bmi')
    list_filter = ('gender',)
    search_fields = ('title', 'description')

# Admin configuration for ProgressReport model
@admin.register(models.ProgressReport)
class ProgressReportAdmin(admin.ModelAdmin):
    list_display = ('customer', 'weight_kg', 'mood', 'created_at')
    list_filter = ('mood', 'created_at')
    search_fields = ('customer__name', 'comments')  # Assuming Customer model has a 'name' field



@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('header', 'created_at', 'updated_at')
    search_fields = ('header',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(models.BlogContents)
class BlogContentsAdmin(admin.ModelAdmin):
    list_display = ('header', 'created_at', 'updated_at')
    search_fields = ('header',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)






# Register Plan model
class PlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'header_text', 'is_popular', 'created_at', 'updated_at')
    search_fields = ('title', 'header_text')
    list_filter = ('is_popular',)
    ordering = ('-created_at',)
    
admin.site.register(models.Plan, PlanAdmin)


class MealPlanDescriptionInline(admin.TabularInline):  # Use TabularInline for a compact view
    model = models.MealPlanDescription
    extra = 1  # Number of empty forms displayed for adding new descriptions
    fields = ['header', 'image', 'description', 'list_item']
    readonly_fields = ['created_at', 'updated_at']  # Optional: Make timestamps read-only


# Register MealPlan model
class MealPlanAdmin(admin.ModelAdmin):
    inlines = [MealPlanDescriptionInline]
    list_display = ('title', 'plan', 'is_popular', 'total_days', 'created_at', 'updated_at')
    search_fields = ('title', 'plan__title')
    list_filter = ('is_popular',)
    ordering = ('-created_at',)

admin.site.register(models.MealPlan, MealPlanAdmin)




# Register MealPlanDescription model
class MealPlanDescriptionAdmin(admin.ModelAdmin):
    list_display = ('header', 'plan', 'created_at', 'updated_at')
    search_fields = ('header', 'plan__title')
    ordering = ('-created_at',)

admin.site.register(models.MealPlanDescription, MealPlanDescriptionAdmin)


# Register DailyPlan model
class DailyPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'mealplan', 'day', 'created_at', 'updated_at')
    search_fields = ('title', 'mealplan__title')
    list_filter = ('mealplan', 'day')
    ordering = ('mealplan', 'day')

admin.site.register(models.DailyPlan, DailyPlanAdmin)


# Register Meal model
class MealAdmin(admin.ModelAdmin):
    list_display = ('meal_type', 'daily_plan','food_type','calories','protein','carbs','fats', 'created_at', 'updated_at')
    search_fields = ('meal_type', 'daily_plan__title')
    list_filter = ('meal_type','food_type')
    ordering = ('-created_at',)

admin.site.register(models.Meal, MealAdmin)
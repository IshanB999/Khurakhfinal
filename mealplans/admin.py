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

# Admin configuration for MealPlan model
@admin.register(models.MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'bmi_range', 'created_at')
    list_filter = ('bmi_range',)
    search_fields = ('name', 'description')
    # readonly_fields = ('created_at', 'updated_at')  # To prevent editing timestamps

# Admin configuration for Food model
@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'plan', 'created_at')
    list_filter = ('plan',)
    search_fields = ('title', 'description')
    # readonly_fields = ('created_at', 'updated_at')

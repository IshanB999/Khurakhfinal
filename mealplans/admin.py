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


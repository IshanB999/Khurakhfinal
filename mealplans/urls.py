
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login_view,name='login'),
    path('bmi-calculator',views.BmiCalculatorView.as_view(),name='calculator'),
    path("logout",views.logout_view,name='logout'),
    path('profile/',views.DashboardView.as_view(),name='profile'),
    path('profile/change-password',views.change_password,name='changepw'),
    
]

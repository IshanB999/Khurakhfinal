
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login_view,name='login'),
    path('bmi-calculator',views.bmi_calculator,name='calculator'),
    path("logout",views.logout_view,name='logout'),
]

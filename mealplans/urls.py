
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index),
    path('signup/',views.signup,name="signup"),
]

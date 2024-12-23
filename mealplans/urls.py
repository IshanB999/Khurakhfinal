
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login_view,name='login'),
    path('bmi-calculator',views.BmiCalculatorView.as_view(),name='calculator'),
    path("logout",views.logout_view,name='logout'),
    path('profile/',views.DashboardView.as_view(),name='profile'),
    path('profile/change-password',views.change_password,name='changepw'),

    # blog

    path('blogs/',views.blog_view,name='blog-view'),
    path('blogs/<int:pk>/',views.blog_content_view,name='blog-content-view'),
    path('meal-planner/',views.pre_meal_plan_view,name='pre-meal-plan'),
    path('meal-planner/<int:pk>/',views.pre_meal_plan_content_view,name='pre-meal-plan-content'),
    path('plan/<int:pk>/',views.daily_plan_view,name='daily-plan-content'),

     path('create-plan/<int:pk>/', views.create_customer_plan, name='create_customer_plan'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

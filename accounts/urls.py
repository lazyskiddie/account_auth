from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_request, name='login_request'),
    path('verify/', views.verify_otp, name='verify_otp'),
]
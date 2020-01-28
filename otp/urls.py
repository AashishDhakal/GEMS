from django.urls import path
from .views import ValidatePhoneSendOTP,ValidateOTP,Register
urlpatterns = [
    path('validatephone/',ValidatePhoneSendOTP.as_view()),
    path('validateotp/',ValidateOTP.as_view()),
    path('register/',Register.as_view()),
]
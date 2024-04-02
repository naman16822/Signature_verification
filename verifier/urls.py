from django import views
from django.urls import path
from verifier.views import verify_signature

urlpatterns = [
    path('verify/', verify_signature, name='verify_signature'),
    
]

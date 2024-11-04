"""
URL mappings for the user API.
"""
from django.urls import path

from user import views

app_name = 'user' # Use for reverse mapping in the test_user_api file

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]
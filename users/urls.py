from django.urls import path
from .views import register, home, CustomLoginView, profile

urlpatterns = [
    path('', home, name='home'),  # Add this line for the root URL
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
]
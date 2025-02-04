from django.urls import path
from .views import home

# Define the URL patterns for the API
urlpatterns = [
    path('', home, name='api-home'), # Define a URL pattern for the home view
]
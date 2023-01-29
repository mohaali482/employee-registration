from django.urls import path

from .views import UserProfile

urlpatterns = [
    path('user-profile/', UserProfile.as_view(), name="user-profile"),
]

from django.urls import path
from .views import *

urlpatterns = [
    path("users/", UserProfileView.as_view(), name="users_detals")
]

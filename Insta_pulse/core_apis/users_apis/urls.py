from django.urls import path
from .views import *

urlpatterns = [
    path("users/", UserView.as_view(), name="users"),
    path("users/<str:username>/", UserProfileView.as_view(), name="users_details")
]

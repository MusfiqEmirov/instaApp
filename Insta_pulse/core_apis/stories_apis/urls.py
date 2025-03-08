from django.urls import path
from .views import *

urlpatterns = [
    path("storys/", StoryView.as_view(), name="story"),
    path("storys/<int:id>/", StoryDetailsView.as_view(), name="story_details"),

    path("storys/<int:story_id>/feedback/", FeedbackCreateView.as_view(), name="feedback_create"),
    path("feedback/<int:feedback_id>/", FeedbackDeleteView.as_view(), name="feedback_delete"),
    path("storys/<int:feedback_id>/likes/", LikeCreateView.as_view(), name="like_create"),
    path("likes/<int:like_id>/", LikeDeleteView.as_view(), name="like_delete")

]

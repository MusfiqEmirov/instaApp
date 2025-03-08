from django.urls import path
from .views import *

urlpatterns = [
    path("posts/", PostView.as_view(), name="posts"),
    path("posts/<int:id>/", PostDetailsView.as_view(), name="posts_details"),

    path("posts/<int:post_id>/comments/", CommentCreateView.as_view(), name="comment_create"),
    path("comments/<int:comment_id>/", CommentDeleteView.as_view(), name="comment_delete"),
    path("posts/<int:post_id>/likes/", LikeCreateView.as_view(), name="like_create"),
    path("likes/<int:like_id>/", LikeDeleteView.as_view(), name="like_delete")


]

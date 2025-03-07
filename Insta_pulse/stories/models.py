from django.db import models
from users.models import User


class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    media = models.FileField(upload_to='stories/')
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"Story by {self.user.username}"
    
    
class StoryComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_comments')
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.story}"    


class StoryLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_likes')
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user.username} on {self.story}"
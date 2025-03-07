from rest_framework import serializers
from .models import *

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"


class StoryCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryComment
        fields = "__all__"


class StoryLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryLike
        fields = "__all__"

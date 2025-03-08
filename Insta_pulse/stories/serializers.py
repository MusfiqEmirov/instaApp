from rest_framework import serializers
from django.core.files.base import ContentFile
import base64 # sekli base 64 ile jsonda sekil adini qeyd etmek ucun

from .models import *


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"


class StoryCreateSerializer(serializers.ModelSerializer):
    media = serializers.CharField(required=False, allow_null=True)
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

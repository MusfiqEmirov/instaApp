from rest_framework import serializers
from django.core.files.base import ContentFile
import base64 # sekli base 64 ile jsonda sekil adini qeyd etmek ucun

from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    image = serializers.CharField(required=False, allow_null=True)
    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

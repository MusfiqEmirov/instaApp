from rest_framework import serializers
from django.core.files.base import ContentFile
import base64 # sekli base 64 ile jsonda sekil adini qeyd etmek ucun

from users.models import *


class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.CharField(required=False, allow_null=True) #
    class Meta:
        model = User
        fields = "__all__"


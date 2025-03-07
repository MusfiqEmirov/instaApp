from rest_framework import generics
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from users.models import User
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from django.http.response import Http404


class UserProfileView(APIView):

    def get(self, requests):
        user_data = User.objects.all()
        serializer = UserSerializer(user_data, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, requests):
        return NotImplemented
    
    def patch(self, requests):
        return NotImplemented

    def delete(self, requests):
        return NotImplemented
    
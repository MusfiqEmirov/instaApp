from rest_framework import generics
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from django.http.response import Http404

from posts.models import Post
from posts.serializers import *


class PostView(APIView):

    def get(self, request):
        post_data = Post.objects.all()
        serializer = PostSerializer(post_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        data = request.data
        post_data = data.get("id", None)
        post_selected_id = Post.objects.filter(pk=post_data).first()
        serializer = PostCreateSerializer(post_selected_id, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = request.data
        post_data = data.get("id", None)
        if post_data:
            post = Post.objects.filter(pk=post_data).first()
            post.delete()
            return Response({"message":"secdiyiniz post artiq siolindi"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"errors":"post tapilmadi"}, status=status.HTTP_400_BAD_REQUEST)
    


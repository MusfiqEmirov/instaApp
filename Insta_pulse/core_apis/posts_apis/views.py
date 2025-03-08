from rest_framework import generics
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from django.http.response import Http404

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import AuthenticationFailed


from posts.models import *
from posts.serializers import *


class PostView(APIView): # post ucunncrud emeliyatlari

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

        # yalniz postun sahibi ede biler
        if post_selected_id.user != request.user and not request.user.is_staff:
            raise PermissionDenied("nu emelyat ucun icazeniz yoxdur")
        serializer = PostCreateSerializer(post_selected_id, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #ancaq postun sahibi sile biler
    def delete(self, request):
        data = request.data
        post_data = data.get("id", None)
        if post_data:
            post = Post.objects.filter(pk=post_data).first()
            if post.user != request.user and not request.user.is_staff:
                raise PermissionDenied("Bu əməliyyat üçün icazəniz yoxdur")
            post.delete()
            return Response({"message":"secdiyiniz post artiq siolindi"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"errors":"post tapilmadi"}, status=status.HTTP_400_BAD_REQUEST)
    

class PostDetailsView(APIView): # idye gore axtriw
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class CommentCreateView(APIView):
    def post(self, request, post_id):
        if not request.user.is_authenticated:
            raise AuthenticationFailed("Bu emelyat ucun daxil olmag lazimdir")
        post = get_object_or_404(Post, id=post_id)
        user = request.user  
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentDeleteView(APIView):
    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        # ancq commetin sahibi sile biler
        if comment.user == request.user or request.user.is_staff:
            comment.delete()
            return Response({"message": "Comment silindi"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "bu emelyat ucun icaze lazimdirr!!!"}, status=status.HTTP_403_FORBIDDEN)    
    

class LikeCreateView(APIView):
    def post(self, request, post_id):
        if not request.user.is_authenticated:
            raise AuthenticationFailed("Bu ə emeleytacun daxilmolmag lazimdir")
        post = get_object_or_404(Post, id=post_id)
        user = request.user  
        # bir istifadeci bir postu birdenartiq beyene bilmez
        if Like.objects.filter(post=post, user=user).exists():
            return Response({"error": "Bu post artiq beyenilib"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LikeDeleteView(APIView):
    def delete(self, request, like_id):
        like = get_object_or_404(Like, id=like_id)
        
        # Yalnız like-in sahibi və ya admin silə bilər
        if like.user == request.user or request.user.is_staff:
            like.delete()
            return Response({"message": "Like silindi"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Bu əməliyyat üçün icazəniz yoxdur"}, status=status.HTTP_403_FORBIDDEN)
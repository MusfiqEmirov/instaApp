from rest_framework import generics
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from django.http.response import Http404

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import AuthenticationFailed


from stories.models import *
from stories.serializers import *


class StoryView(APIView): # post ucunncrud emeliyatlari

    def get(self, request):
        story_data = Story.objects.all()
        serializer = StorySerializer(story_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        data = request.data
        story_data = data.get("id", None)
        story_selected_id = Story.objects.filter(pk=story_data).first()

        # yalniz stroyr sahibi ede biler
        if story_selected_id.user != request.user and not request.user.is_staff:
            raise PermissionDenied("nu emelyat ucun icazeniz yoxdur")
        serializer = StoryCreateSerializer(story_selected_id, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #ancaq stroyr sahibi sile biler
    def delete(self, request):
        data = request.data
        story_data = data.get("id", None)
        if story_data:
            story = Story.objects.filter(pk=story_data).first()
            if story.user != request.user and not request.user.is_staff:
                raise PermissionDenied("Bu əməliyyat üçün icazəniz yoxdur")
            story.delete()
            return Response({"message":"secdiyiniz story artiq siolindi"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"errors":"story tapilmadi"}, status=status.HTTP_400_BAD_REQUEST)
    

class StoryDetailsView(APIView): # idye gore axtriw
    def get(self, request, id):
        story = get_object_or_404(Story, id=id)
        serializer = StorySerializer(story)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class FeedbackCreateView(APIView):
    def post(self, request, feedback):
        if not request.user.is_authenticated:
            raise AuthenticationFailed("Bu emelyat ucun daxil olmag lazimdir")
        story = get_object_or_404(Story, id=feedback)
        user = request.user  
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=story, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    





























    
    
# class FeedbackDeleteView(APIView):
#     def delete(self, request, feedback_id):
#         comment = get_object_or_404(Story, id=feedback_id)
#         # ancq feedbackin  sahibi sile biler
#         if comment.user == request.user or request.user.is_staff:
#             comment.delete()
#             return Response({"message": "Comment silindi"}, status=status.HTTP_204_NO_CONTENT)
#         return Response({"error": "bu emelyat ucun icaze lazimdirr!!!"}, status=status.HTTP_403_FORBIDDEN)    
    

# class LikeCreateView(APIView):
#     def post(self, request, post_id):
#         if not request.user.is_authenticated:
#             raise AuthenticationFailed("Bu ə emeleytacun daxilmolmag lazimdir")
#         post = get_object_or_404(Post, id=post_id)
#         user = request.user  
#         # bir istifadeci bir postu birdenartiq beyene bilmez
#         if Like.objects.filter(post=post, user=user).exists():
#             return Response({"error": "Bu post artiq beyenilib"}, status=status.HTTP_400_BAD_REQUEST)
#         serializer = LikeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(post=post, user=user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class LikeDeleteView(APIView):
#     def delete(self, request, like_id):
#         like = get_object_or_404(Like, id=like_id)
        
#         # Yalnız like-in sahibi və ya admin silə bilər
#         if like.user == request.user or request.user.is_staff:
#             like.delete()
#             return Response({"message": "Like silindi"}, status=status.HTTP_204_NO_CONTENT)
#         return Response({"error": "Bu əməliyyat üçün icazəniz yoxdur"}, status=status.HTTP_403_FORBIDDEN)
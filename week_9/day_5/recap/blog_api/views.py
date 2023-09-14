from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView, Response
from blog.models import Blog
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class BlogList(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Blog.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    
    def post(self,request,format=None):
        serializers = BlogSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorNames(APIView):
    def post(self,request,format=None):
        serializers = AuthorSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentQuoi(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    
    def post(self,request,format=None):
        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    
    

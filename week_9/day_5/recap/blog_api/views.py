from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView, Response
from blog.models import Blog
from .serializers import PostSerializer

# Create your views here.


class PostList(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Blog.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return JsonResponse(data=serializer.data, safe=False)

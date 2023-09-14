from rest_framework import serializers
from blog.models import Blog,Author,Comment


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
from rest_framework import serializers
from .models import Post, PostImage

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image', 'caption']

class PostListSerializer(serializers.ModelSerializer):
    summary = serializers.SerializerMethodField()
    category_display = serializers.CharField(source='get_category_display', read_only=True)  
    images = PostImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ['title', 'slug', 'created_at', 'category', 'category_display', 'summary', 'images']

    def get_summary(self, obj):
        return ' '.join(obj.content.split()[:25]) + '...'

class PostDetailSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True) 
    category_display = serializers.CharField(source='get_category_display', read_only=True)  

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'created_at', 'category', 'category_display', 'images']

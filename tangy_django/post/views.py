from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer

class PostList(APIView):
    def get(self, request, format=None):
        category = request.GET.get('category', None)
        posts = Post.objects.all()
        if category:
            posts = posts.filter(category=category)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

class PostDetail(APIView):
    def get_object(self, slug):
        try:
            return Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        post = self.get_object(slug)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

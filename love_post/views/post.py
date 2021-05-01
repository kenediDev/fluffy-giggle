from django.utils.translation import gettext as _
from rest_framework import status, permissions, parsers, generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from database.models.post import Post
from love_post.serializer.post_serializer import PostSerializer, PostModelSerializer
from love_post.utils.filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend

class PostGenericsAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = [permissions.AllowAny,]
    filter_backends = [DjangoFilterBackend,] 
    filterset_class = PostFilter


class UpdateAPIView(APIView):
    queryset = Post.objects.all()
    serializer_query = PostSerializer
    parser_classes = [parsers.MultiPartParser, parsers.JSONParser,]

    def post(self,r,pk):
        queryset = self.queryset.filter(public_id=pk).first()
        serializer = self.serializer_query(queryset,data=r.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": _("Post has been updated")},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PostModelViewSets(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    serializer_query = PostSerializer
    parser_classes = [parsers.MultiPartParser, parsers.JSONParser,]
    
    def get_permissions(self):
        if self.action == "create":
            permission_classes = [permissions.IsAuthenticated,]
        else:
            permission_classes = [permissions.AllowAny,]
        return [permission() for permission in permission_classes]

    def list(self,r):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,r):
        serializer = self.serializer_query(data=r.data)
        serializer.context['args'] = 'create'
        if serializer.is_valid():
            serializer.save()
            post = self.queryset.filter(author=r.user).last()
            get_serializer = self.serializer_class(post)
            return Response(get_serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,r,pk):
        queryset = self.get_queryset().filter(public_id=pk).first()
        if not queryset:
            return Response({'message': _("Post not found")},status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

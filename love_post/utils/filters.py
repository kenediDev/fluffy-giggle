from django_filters import rest_framework as filters
from database.models.post import Post

class PostFilter(filters.FilterSet):
    content = filters.filters.CharFilter(lookup_expr="icontains",field_name="content")

    class Meta:
        model = Post
        fields = ["content",]



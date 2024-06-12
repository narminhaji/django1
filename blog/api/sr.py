from rest_framework import sr
from ..models import Blog

class BlogSerializer(sr.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
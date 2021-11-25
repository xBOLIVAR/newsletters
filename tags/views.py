from django.db.models import query
from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from tags.serializers import TagSerializer
from tags.models import Tag

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_class = (AllowAny,)


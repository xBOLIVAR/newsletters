from rest_framework.permissions import AllowAny, IsAdminUser
from tags.serializers import TagSerializer
from rest_framework.viewsets import ModelViewSet
from tags.models import Tag

# Create your views here.

class TagViewSet(ModelViewSet):  
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)    #(IsAdminUser,) 

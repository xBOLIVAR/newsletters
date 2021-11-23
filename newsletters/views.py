from rest_framework.permissions import AllowAny, IsAdminUser
from newsletters.serializers import NewsletterSerializer
from rest_framework.viewsets import ModelViewSet
from newsletters.models import Newsletter

# Create your views here.

class NewsletterViewSet(ModelViewSet):  
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = (AllowAny,)    #(IsAdminUser,) 
from rest_framework.permissions import AllowAny, IsAdminUser
from newsletters.serializers import NewsletterSerializer
from rest_framework.viewsets import ModelViewSet
from newsletters.models import Newsletter

# Create your views here.

class NewsletterViewSet(ModelViewSet):  
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = (AllowAny,)    #(IsAdminUser,) 

    def get_serializer_class(self):
        if self.action == 'list' and not self.request.user.is_staff:
            return NewsletterSerializer #LibroSerializer

        if self.request.method == 'POST':
            return NewsletterSerializer

        if self.action == 'retrieve' and self.request.user.is_staff:
            return NewsletterSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from newsletters.serializers import NewsletterSerializer
from rest_framework.viewsets import ModelViewSet
from newsletters.models import Newsletter

# Create your views here.

class NewsletterViewSet(ModelViewSet):  
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        try:
            data = {}
            for i in self.request.query_params:
                print(i, self.request.query_params[i])
                data[i] = self.request.query_params[i]
            return self.queryset.filter(**data)
        except Exception as e:
            return self.queryset

            
        


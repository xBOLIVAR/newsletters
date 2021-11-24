from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from newsletters.serializers import NewsletterSerializer, NewsletterNoAdminSerializer
from rest_framework.viewsets import ModelViewSet
from newsletters.models import Newsletter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

# Create your views here.

class NewsletterViewSet(ModelViewSet):  
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)    #(IsAdminUser,) 

    def get_serializer_class(self):
        print(self.request.user.is_staff)
        # si es admin, get post, accion de invitar a otros admin a editar
        if  self.request.user.is_staff:
            return NewsletterSerializer 

        #si no es admin y get
        if self.action == 'list' and not self.request.user.is_staff:
            return NewsletterNoAdminSerializer 

        #si no es admin y el boletin paso la meta = SUSCRIBIR

        #si no es admin y el boletin no paso la meta = VOTAR

    """@action(methods=['POST'], detail=True)
    def publicar(self, request, pk=None):
        newsletter = self.get_object()
        newsletter.save()

        if Newsletter.votos > meta:
            return publicar

        if Newsletter.votos < meta:
            return "no ha llegado a la meta"""

        

    def get_queryset(self):
        try:
            data = {}
            for i in self.request.query_params:
                print(i, self.request.query_params[i])
                data[i] = self.request.query_params[i]
            return self.queryset.filter(**data)
        except Exception as e:
            return self.queryset

    
       
        


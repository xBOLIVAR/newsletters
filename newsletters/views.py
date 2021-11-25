from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from newsletters.serializers import NewsletterSerializer, NewsletterNoAdminSerializer
from rest_framework.viewsets import ModelViewSet
from newsletters.models import Newsletter
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.mail import send_mail

from usuarios.serializers import UserSerializer


# Create your views here.

class NewsletterViewSet(ModelViewSet):  
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = (AllowAny,)    #(IsAdminUser,) 

    def get_serializer_class(self):
        print(self.request.user.is_staff)
        # si es admin, get post, accion de invitar a otros admin a editar
        if  self.request.user.is_staff:


            return NewsletterSerializer 

        #si no es admin y get
        if self.action == 'list' and not self.request.user.is_staff:
            return NewsletterNoAdminSerializer 


    def get_queryset(self):
        try:
            data = {}
            for i in self.request.query_params:
                print(i, self.request.query_params[i])
                data[i] = self.request.query_params[i]
            return self.queryset.filter(**data)
        except Exception as e:
            return self.queryset

    @action(methods=['GET','POST'], detail=True)
    def votar(self, request, pk=None):
        if request.method == 'GET':
            newsletters = Newsletter.objects.get(id=pk)
            votos  = newsletters.votos.all()
            serialized = UserSerializer(votos, many = True)
            return Response(
                status = status.HTTP_200_OK,
                data = serialized.data
            )
        
        if request.method == 'POST':
            ids = request.data['usuarios_ids']
            print(ids)
            newsletters = Newsletter.objects.get(id=pk)
            print(newsletters)
            for i in ids:
                votos = newsletters.votos.add(i)

            return Response(status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True)
    def publicar(self, request, pk=None):
        if request.method == 'POST':
            newsletters = Newsletter.objects.get(id=pk)
            votos = newsletters.votos.count()
            if votos >= newsletters.meta:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    @action(methods=['POST'], detail=True)
    def suscribirse(self, request, pk=None):
        newsletters = Newsletter.objects.get(id=pk)
        meta = newsletters.meta.count()
        if meta >= 5:
            return Response(status=status.HTTP_200_OK)
        
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


    


    
       
        


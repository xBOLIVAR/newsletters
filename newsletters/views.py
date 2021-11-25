from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from newsletters.serializers import NewsletterSerializer, NewsletterNoAdminSerializer
from rest_framework.viewsets import ModelViewSet
from newsletters.models import Newsletter
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.mail import send_mail

from usuarios.serializers import UserSerializer


# Create your views here.

class NewsletterViewSet(ModelViewSet):  
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    # permission_classes = (AllowAny,)    #(IsAdminUser,) 

    def get_serializer_class(self):
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
            newsletters = Newsletter.objects.get(id=pk)

            for i in ids:
                newsletters.votos.add(i)

            return Response(status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True)
    def publicar(self, request, pk=None):
        if request.method == 'POST':
            newsletters = Newsletter.objects.get(id=pk)
            votos = newsletters.votos.count()
            if votos >= newsletters.meta:
                newsletters.publicar = True
                newsletters.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    @action(methods=['POST', 'GET'], detail=True)
    def suscribirse(self, request, pk=None):
        newsletters = Newsletter.objects.get(id=pk)
        user_id = self.request.user.id 

        


        if request.method == 'POST':
            if newsletters.publicar:
                newsletters.suscrito.add(user_id)

                send_mail(
                    subject = 'Hay Nuevas noticias',
                    message = f'Tenemos nuevas noticias en {newsletters.nombre}',
                    from_email = 'newsletters@gmail.com',
                    recipient_list= [self.request.user.email],
                    html_message= f'<h1> Tenemos nuevas noticas en: {newsletters.nombre}</h1>'
                )

                return Response(status=status.HTTP_200_OK)
            
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if request.method == 'GET':
            print(self.request.user.email)
            return Response(status=status.HTTP_200_OK)

        
    
       
        


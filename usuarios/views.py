from rest_framework.permissions import AllowAny, IsAdminUser
from usuarios.serializers import UsuarioSerializer
from rest_framework.viewsets import ModelViewSet
from usuarios.models import Usuario

# Create your views here.

class UsuarioViewSet(ModelViewSet):  
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (AllowAny,)    #(IsAdminUser,) 
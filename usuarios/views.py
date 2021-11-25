from rest_framework.permissions import AllowAny, IsAdminUser
from newsletters.models import Newsletter
from usuarios.serializers import UsuarioSerializer
from rest_framework.viewsets import ModelViewSet
from usuarios.models import Usuario

# Create your views here.

class UsuarioViewSet(ModelViewSet):  
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
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

        
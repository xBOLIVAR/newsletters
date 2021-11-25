from rest_framework.permissions import AllowAny, IsAdminUser
from usuarios.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

# Create your views here.

class UsuarioViewSet(ModelViewSet):  
    queryset = User.objects.all()
    serializer_class = UserSerializer
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

        
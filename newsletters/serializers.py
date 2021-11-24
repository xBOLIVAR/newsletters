from rest_framework.serializers import ModelSerializer
from newsletters.models import Newsletter

# si es admin, get post, accion de invitar
class NewsletterSerializer(ModelSerializer):

    class Meta:
        model = Newsletter
        fields = '__all__'


#si no es adminn  get
class NewsletterNoAdminSerializer(ModelSerializer):

    class Meta:
        model = Newsletter
        fields = ['nombre', 'descripcion', 'imagen', 'votar']


#si no es admin y el boletin paso la meta = SUSCRIBIR

#si no es admin y el boletin no paso la meta = VOTAR


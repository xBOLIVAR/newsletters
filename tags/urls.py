from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from tags.views import TagViewSet

router = DefaultRouter()
router.register('tags', TagViewSet)

urlpatterns = router.urls
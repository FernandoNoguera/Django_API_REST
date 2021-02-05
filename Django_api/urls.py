from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from personajes.views import PersonajesViewSets, ChelasViewSet

router = DefaultRouter()
router.register('personajes', PersonajesViewSets)
router.register('chelas', ChelasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
  
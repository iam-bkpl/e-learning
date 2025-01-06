from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BatchViewSet

router = DefaultRouter()
router.register("batch", BatchViewSet)


urlpatterns = [path("", include(router.urls))]

from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import UploadViewSet

router = DefaultRouter()
router.register(r'chatvibe-upload',UploadViewSet ,basename='chatvibe-upload')

urlpatterns = [
    path('', include(router.urls)),
]

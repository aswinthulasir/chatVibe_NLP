from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import UploadViewSet,home

router = DefaultRouter()
router.register(r'upload', UploadViewSet ,basename='chatvibe-upload')

urlpatterns = [
    path('', home, name='homepage'),
    path('', include(router.urls)),
]

from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from .models import chat_upload
from .serializers import Uploadserializer


class UploadViewSet(viewsets.ModelViewSet):
    queryset = chat_upload.objects.all()
    serializer_class = Uploadserializer


        
    


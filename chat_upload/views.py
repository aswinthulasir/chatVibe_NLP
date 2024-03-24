from django.shortcuts import render
from rest_framework import viewsets
import requests
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .models import chat_upload
from .serializers import Uploadserializer


class UploadViewSet(viewsets.ModelViewSet):
    queryset = chat_upload.objects.all()
    serializer_class = Uploadserializer

    def create(self, request, *args, **kwargs):
        if not request.data.get('chat_file'):
            return Response({"error": "No file found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)  # Validate data
            self.perform_create(serializer)
            headers = self.get_success_header(serializer.data)
            return Response({"success": "File found"}, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save()

        
    


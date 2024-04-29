from django.shortcuts import render
from rest_framework import viewsets
import requests
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .models import chat_upload
from .serializers import Uploadserializer
from utils import data_preprocess,txt_csv,resultmodel
def home(request):
    return render(request, 'index.html')

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

    #returns emotion of the text    
    def list(self, request, *args, **kwargs):
        input_file = request.data.get('chat_file')
        if not input_file:
            return Response({"error": "No file found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = txt_csv.csv_txt(input_file)
            data = data_preprocess.preprocess_text(input_file)
            data = resultmodel.emotionlabel(data)
            return Response(data, status=status.HTTP_200_OK)

        
    


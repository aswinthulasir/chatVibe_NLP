from django.shortcuts import render
from rest_framework import viewsets
import requests
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .models import chat_upload
from .serializers import Uploadserializer
from utils import data_preprocess,txt_df,resultmodel
def home(request):
    return render(request, 'index1.html')

class UploadViewSet(viewsets.ModelViewSet):
    queryset = chat_upload.objects.all()
    serializer_class = Uploadserializer

    def create(self, request, *args, **kwargs):
        serializer = Uploadserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request, *args, **kwargs):
        queryset = chat_upload.objects.all()
        print(queryset)
        print("hello world")
        input_file = queryset.values('chat_file','Name','chat_startdate','chat_enddate')
        #if input file is not found return error
        if not input_file:
            return Response({"error": "No file found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            file = input_file[0]['chat_file']
            Name = input_file[0]['Name']
            chat_startdate = input_file[0]['chat_startdate']
            chat_enddate = input_file[0]['chat_enddate']
            df = txt_df.text_to_df(file,Name,chat_startdate,chat_enddate)
            df1 = data_preprocess.preprocess_text(df)
            df2 = resultmodel.emotionlabel(df1)

            #delete table row
            queryset.delete()
            return Response(df2, status=status.HTTP_200_OK)
        
    


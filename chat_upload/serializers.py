from rest_framework import serializers
from .models import chat_upload

class Uploadserializer(serializers.ModelSerializer):
    class Meta:
        model = chat_upload
        fields = ('__all__')

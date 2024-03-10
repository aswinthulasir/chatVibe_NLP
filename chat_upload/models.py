from django.db import models

# Create your models here.
class chat_upload(models.Model):
    chat_id = models.AutoField(primary_key=True)
    chat_file = models.FileField(upload_to='chat_files/')
    chat_startdatetime = models.DateTimeField()
    chat_startampm = models.CharField(max_length=2)
    chat_enddatetime = models.DateTimeField()
    chat_endampm = models.CharField(max_length=2)

    def __str__(self):
        return self.chat_id
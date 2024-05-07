from django.db import models

# Create your models here.
class chat_upload(models.Model):
    chat_id = models.AutoField(primary_key=True)
    chat_file = models.FileField(upload_to='data/ipdata/', blank=False)
    Name = models.CharField(max_length=100, null=True, blank=True)
    chat_startdate = models.DateField(null=True, blank=True)
    chat_enddate = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.Name
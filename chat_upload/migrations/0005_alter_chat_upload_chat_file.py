# Generated by Django 5.0.2 on 2024-04-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_upload', '0004_chat_upload_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_upload',
            name='chat_file',
            field=models.FileField(blank=True, null=True, upload_to='chat_files/chat.txt'),
        ),
    ]

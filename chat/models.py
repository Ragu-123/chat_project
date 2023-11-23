from django.db import models

class ChatUser(models.Model):
    name = models.CharField(max_length=255)

class ChatMessage(models.Model):
    user = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    content = models.TextField()

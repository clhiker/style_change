from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username
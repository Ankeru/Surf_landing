from django.db import models

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()

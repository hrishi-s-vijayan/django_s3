from django.db import models


class File(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')

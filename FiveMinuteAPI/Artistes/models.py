from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    stage_name = models.CharField(unique=True, max_length=100)

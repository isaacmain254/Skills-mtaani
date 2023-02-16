from django.db import models

# Create your models here.
# Freelancer model
class Freelancers(models.Model):
    name = models.CharField(max_length=60)

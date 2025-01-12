from django.db import models

# Create your models here.

class List(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, default="pending")
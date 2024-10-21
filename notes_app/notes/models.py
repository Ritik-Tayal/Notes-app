from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='notes')
    
    class Meta:
        ordering=['-updated','-created']
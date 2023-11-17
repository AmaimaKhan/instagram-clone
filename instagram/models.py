from django.db import models

# Create your models here.

class profile(models.Model):
    name= models.CharField (max_length=15, blank=False)
    bio= models.TextField ()

# def __str__(self):
#     return f'profile from {self.name}, bio: {self.bio}'
    

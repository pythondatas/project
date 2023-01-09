from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='images')
    desc=models.TextField()
class fourimages(models.Model):
    name=models.CharField(max_length=200)
    images=models.ImageField(upload_to='photos')
    description=models.TextField()
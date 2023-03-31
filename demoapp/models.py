from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
          return self.name

class people(models.Model):
    name1=models.CharField(max_length=250)
    image1=models.ImageField(upload_to='pics')
    desc1=models.TextField()

    def __str__(self):
        return self.name1

class picture(models.Model):
    name2=models.CharField(max_length=250)
    image2=models.ImageField(upload_to='pics')
    desc2 =models.TextField()
    def __str__(self):
        return self.name2
from django.db import models

# Create your models here.
class app_one_person(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    Class = models.CharField(max_length=50)    
    images = models.ImageField(upload_to="image",default="")
    def __str__(self):
        return self.name

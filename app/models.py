from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50,unique=True)
    phone_number = models.IntegerField()
    email=models.EmailField()
    # profile_pic = models.ImageField(upload_to='profile_pic/',null=True,blank=True)
    password=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
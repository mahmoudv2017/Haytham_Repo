from django.db import models

from django.contrib.auth.admin import User

# Create your models here.

class products(models.Model):
    picture = models.ImageField(upload_to = "Product_image/" , blank = True )
    #specification = models.JSONField()
    name = models.CharField( max_length = 250 , blank=True)
    slug = models.CharField( max_length = 250 , blank=True)
    desc = models.CharField( max_length = 250 , blank=True)
    special = models.BooleanField(default=False)
    typer = [
        ("lp" , "laptop"),
        ("pc" , "pc case"),
        ("special" , "special line")
    ]
    typpe = models.CharField(max_length= 20 , choices = typer , blank = True)
   
    
    price = models.FloatField(default=0)

   

    details = models.JSONField(default = dict)

    def __str__(self):
        return self.name


class acounter(models.Model):
    user = models.OneToOneField(User , on_delete= models.CASCADE)
    user_rating = models.JSONField(default = dict)

    def __str__(self):
        return self.user.username
    
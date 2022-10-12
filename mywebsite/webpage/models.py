 
 
from django.db import models
# from django.db.models.base import Model
from datetime import datetime
from django.contrib.auth.models import User



# Create your models here

class blog(models.Model):
    pass
    # name = models.CharField(max_length=100)
    # tagline = models.TextField()

    
        
class post(models.Model):
    title=models.CharField(max_length=200)
    body=models.CharField(max_length=1000)
    created_at=models.DateTimeField(default=datetime.now,blank=True)

    pass



class Profile(models.Model):
    # User=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    pass
    
class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    # reporter = models.ForeignKey(Reporter)

class Contact(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email_address =models.EmailField(max_length = 150)
	message = models.CharField(max_length = 2000)




    





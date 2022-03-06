from django.db import models

# Create your models here.

class signup_table(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    yearofjoining= models.IntegerField()
    registration= models.CharField(max_length=100,default=123)
    pwd=models.CharField(max_length=100,default=123)
   
    # this is useful in admin
    def __str__(self):
        return f'{self.firstname} {self.lastname}'



class faculty_signup(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    coursecode= models.CharField(max_length=20)
    registration= models.CharField(max_length=100,default=123)
    classnumber=models.CharField(max_length=20)
    pwd=models.CharField(max_length=100,default=123)
   
    # this is useful in admin
    def __str__(self):
        return f'{self.firstname} {self.lastname}'

         
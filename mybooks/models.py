from django.db import models

class Customer(models.Model):
    email=models.TextField(max_length=100)
    password=models.TextField(max_length=100)

class Books(models.Model):
    name=models.TextField(max_length=200,null=True)
    image=models.ImageField(upload_to="photos",null=True)
    review=models.TextField(max_length=1000,null=True)
class liked(models.Model):
  
    book=models.ForeignKey(Books,on_delete=models.CASCADE)

    
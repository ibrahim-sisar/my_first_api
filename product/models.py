from django.db import models

# Create your models here.
class CRUDS(models.Model):
    title=models.CharField(max_length=100,default='')
    price=models.IntegerField(default=0)
    taxes=models.IntegerField(default=0,null=True,blank=True)
    ads=models.IntegerField(default=0,null=True,blank=True)
    discount=models.IntegerField(default=0,null=True,blank=True)
    total=models.IntegerField(default=0)
    category=models.CharField(max_length=100,default='')

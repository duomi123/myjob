from django.db import models

# Create your models here.
class Userinfo(models.Model):
    name = models.CharField(max_length=30,default='')
    pwd = models.CharField(max_length=40,default='')
    email =models.CharField(max_length=30,default='')
    receiver =models.CharField(max_length=10,default='')
    address =models.CharField(max_length=60,default='')
    postcode =models.CharField(max_length=6,default='')
    telephone = models.CharField(max_length=11,default='')

    class Meta:
        db_table = 'userinfo'





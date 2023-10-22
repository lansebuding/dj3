from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)
    age = models.IntegerField()
    # data = models.CharField(null=True,blank=True,max_length=64)
    # data2=models.IntegerField(default=3)

# class Depart(models.Model):
#     objects = models.Manager()
#     data=models.IntegerField(default=6)


# UserInfo.objects.create(user="admin",pwd="123456",age=25)
# UserInfo.objects.create(user="YJW",pwd="aaa123456",age=24)

from django.db import models
from user.models import User
from django.utils import timezone

# Create your models here.
class Lab(models.Model):
    admin_id = models.CharField(max_length=10,null=False)
    lab_name = models.CharField(max_length=21,null=False)
    introduce = models.CharField(max_length=1000,null=False)
    members = models.ManyToManyField(User)
    member_num = models.IntegerField(default=0)
    address = models.CharField(max_length=20,null=False,default="")
    is_public = models.BooleanField(default=True) # 是否公开自己的博客
    img = models.IntegerField(default=1) # 展示的图片
    # 图片待加

class Aaya(models.Model):
    aya = models.CharField(max_length=30) # 注册码，由admin管理
    is_used = models.BooleanField(default=False)
    # 失效时间1天
    create_time = models.DateTimeField(default=timezone.now)

class Apply(models.Model):
    user = models.ForeignKey(User,null=False)
    lab = models.ForeignKey(Lab,null=False)
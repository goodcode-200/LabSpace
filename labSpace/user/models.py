from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):   #网站注册用户
    uid = models.CharField("用户哈希值",max_length=25,primary_key=True)
    user = models.OneToOneField(User)  #账号名，密码，邮箱
    is_gov = models.NullBooleanField("用户身份") #支持三种字段，null:游客,true:实验室管理员,false:实验室普通成员
    sex_is = (
        ('man', '男'),
        ('woman', '女'),
    )
    sex = models.CharField("性别", max_length=10, choices=sex_is)
    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name_plural = '网站注册用户'
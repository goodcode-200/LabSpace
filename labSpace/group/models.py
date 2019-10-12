from django.db import models
from django.contrib.auth.models import Group
from user.models import UserProfile

# Create your models here.
class LabGroup(models.Model):
    group = models.OneToOneField(Group)
    admin_tors = models.ManyToManyField(UserProfile,related_name="admins")
    members = models.ManyToManyField(UserProfile,related_name="members")
    member_num = models.IntegerField("成员数目",default=0)
    is_public = models.BooleanField("是否公开")
    def __str__(self):
        return str(self.group)
    class Meta:
        verbose_name_plural = '用户群组'

class LabDetail(models.Model):
    lab = models.ForeignKey(LabGroup)
    desc = models.TextField("团体描述", max_length=3000, default="该团体很懒，暂时没有介绍呢~~")
    class Meta:
        verbose_name_plural = '实验室详情'

class Book(models.Model):
    bookname = models.CharField("书名",max_length=30)
    author = models.CharField("作者",max_length=25)
    publisher = models.CharField("出版社",max_length=35)
    lab = models.ForeignKey(LabDetail)
    def __str__(self):
        return self.bookname
    class Meta:
        verbose_name_plural = '实验室拥有书籍'

# 此标签为所有实验室和其中的方向所共用，便于查询
class MajorTag(models.Model):
    tag_name = models.CharField("主攻内容标签",max_length=20,primary_key=True)
    def __str__(self):
        return self.tag_name
    class Meta:
        verbose_name_plural = '主攻内容标签(公用)'

class Direction(models.Model):
    d_name = models.CharField("研究方向",max_length=20)
    leader = models.ForeignKey(UserProfile)
    lab = models.ForeignKey(LabDetail)
    major_tags = models.ManyToManyField(MajorTag)
    def __str__(self):
        return self.d_name
    class Meta:
        verbose_name_plural = '各实验室主攻方向'

class Honor(models.Model):
    h_name = models.CharField("荣誉名字",max_length=30)
    get_time = models.DateField("获得时间")
    direction = models.ForeignKey(Direction)
    owers = models.ManyToManyField(UserProfile)
    def __str__(self):
        return self.h_name
    class Meta:
        verbose_name_plural = '实验室荣誉获得'

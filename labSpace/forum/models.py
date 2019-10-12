from django.db import models
from user.models import UserProfile
from django.utils import timezone

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField("标签名",max_length=15,primary_key=True)
    def __str__(self):
        return self.tag_name
    class Meta:
        verbose_name_plural = '主题的标签'

class Title(models.Model):
    title = models.CharField("题目",max_length=30,null=False)
    content = models.TextField("内容",max_length=1000,null=False)
    userprofile = models.ForeignKey(UserProfile,null=False)
    pub_time = models.DateTimeField("发布时间",default=timezone.now)
    tags = models.ManyToManyField(Tag)
    comment_num = models.IntegerField("评论数量",default=0)
    like_num = models.IntegerField("点赞数量",default=0)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = '论坛主题'

class Comment(models.Model):
    userprofile = models.ForeignKey(UserProfile,null=False)
    pub_time = models.DateTimeField("发布时间",default=timezone.now)
    title = models.ForeignKey(Title,null=False)
    content = models.CharField("评论内容",max_length=250,null=False)
    like_num = models.IntegerField("点赞数",default=0)
    #  recomments = models.ForeignKey() 评论的评论，先不实现
    class Meta:
        verbose_name_plural = '对于主题的评论'
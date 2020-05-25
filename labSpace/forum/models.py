from django.db import models
from user.models import User
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
    author = models.ForeignKey(User,null=False)
    pub_time = models.DateTimeField("发布时间",default=timezone.now)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.title
    @property
    def show_tags(self):  #构造生成器，展示一个title对象的多对多关系-->tag
        return (i for i in self.tags.all())
    class Meta:
        verbose_name_plural = '论坛主题'
        ordering = ('-pub_time',)
from django.db import models
from django.utils import timezone
from user.models import User
from lab.models import Lab


# Create your models here.
class Blog(models.Model):
    title = models.CharField('题目',max_length=20,null=False)
    link = models.CharField('链接',max_length=5000,null=False)
    author = models.ForeignKey(User)
    lab = models.ForeignKey(Lab)
    add_date = models.DateTimeField('创建日期',default=timezone.now)
    like_num = models.IntegerField('推荐数',default=0)

    class Meta:
        ordering = ('-add_date',)




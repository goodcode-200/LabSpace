from django.db import models
from django.contrib.auth.models import Group,User

# Create your models here.
class LabGroup(models.Model):
	group = models.OneToOneField(Group)
	admin_tor = models.ManyToManyField(User)
	desc = models.CharField("团体描述",max_length=300,default="该团体很懒，暂时没有介绍呢~~")
	def __str__(self):
		return str(self.group)
	class Meta:
		verbose_name_plural = '用户群组'
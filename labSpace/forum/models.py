from django.db import models

# Create your models here.
class Title(models.Model):
	title = models.CharField("题目",max_length=30,null=False)
	content = models.TextField("内容",max_length=1000,null=False)
	def __str__(self):
		return str(self.title)
	class Meta:
		verbose_name_plural = '论坛主题'
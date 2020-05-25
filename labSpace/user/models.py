from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'user'

    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=10,null=False,unique=True,default="用户")
    name = models.CharField(max_length=10,null=False)
    email = models.CharField(max_length=64,null=False)
    email_checked = models.BooleanField(default=False)
    password = models.CharField(max_length=128,null=False)

    def __repr__(self):
        return "{} {} {}".format(self.id, self.nickname, self.name)

    __str__ = __repr__

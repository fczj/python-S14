from django.db import models

# Create your models here.

class UserGroup(models.Model):
    caption = models.CharField(max_length=30)

class UserInfo(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    group_id = models.ForeignKey("UserGroup")
    user_type_choices = (
        (1, '超级用户'),
        (2, '普通用户'),
        (3, '普普通用户'),
    )
    user_type_id = models.IntegerField(choices=user_type_choices,default=1)

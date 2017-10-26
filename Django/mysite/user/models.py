from django.db import models

# Create your models here.



class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    capation = models.CharField(max_length=200)

class UserInfo(models.Model):
    username = models.CharField(max_length=32,blank=True,verbose_name='用户名')
    password = models.CharField(max_length=60, help_text='pwd')
    # user_group_id 数字
    user_group = models.ForeignKey("UserGroup",to_field='uid') # (uid,catption,ctime,uptimew)
    user_type_choices = (
        (1, '超级用户'),
        (2, '普通用户'),
        (3, '普普通用户'),
    )
    user_type_id = models.IntegerField(choices=user_type_choices,default=1)
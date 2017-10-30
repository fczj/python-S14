from django.db import models
# Create your models here.



class Business(models.Model):
    caption = models.CharField(max_length=50)
    code = models.CharField(max_length=50,default='SA',null=True)

class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=50,db_index=True)
    ip = models.GenericIPAddressField(protocol='ipv4',db_index=True)
    port = models.BigIntegerField()
    b = models.ForeignKey(to="Business",to_field='id')

class Application(models.Model):
    name = models.CharField(max_length=50)
    r = models.ManyToManyField("Host")

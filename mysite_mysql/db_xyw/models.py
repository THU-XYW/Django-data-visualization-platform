from django.db import models

# Create your models here.
class Person(models.Model):
    UserName=models.CharField(max_length=200,default='zhangsan',null=True)
    NickName=models.CharField(max_length=200,default='张三',null=True)
    keyNumber=models.CharField(max_length=200,default=20160000,null=True)
    sex=models.CharField(max_length=200,default='男',null=True)
    age=models.IntegerField(default=18,null=True)
    height=models.FloatField(default=170.0,null=True)
    weight=models.FloatField(default=60.0,null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)

class TempPerson(models.Model):
    UserName=models.CharField(max_length=200,default='zhangsan',null=True)
    NickName=models.CharField(max_length=200,default='张三',null=True)
    keyNumber=models.CharField(max_length=200,default=20160000,null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)
class TempPerson2(models.Model):
    UserName=models.CharField(max_length=200,default='zhangsan',null=True)
    NickName=models.CharField(max_length=200,default='张三',null=True)
    keyNumber=models.CharField(max_length=200,default=20160000,null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)


class Administrator(models.Model):
    UserName=models.CharField(max_length=200,default='zhangsan',null=True)
    NickName=models.CharField(max_length=200,default='张三',null=True)
    keyNumber=models.CharField(max_length=200,default=20160000,null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)

class Advanced_Person(models.Model):
    UserName=models.CharField(max_length=200,default='zhangsan',null=True)
    NickName=models.CharField(max_length=200,default='张三',null=True)
    keyNumber=models.CharField(max_length=200,default=20160000,null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)

class Authorize(models.Model):
    Master=models.CharField(max_length=200,default='zhangsan',null=True)
    PersonName=models.CharField(max_length=200,default='张三',null=True)

class Environment(models.Model):
    temperature=models.FloatField(default='18.001',null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)#更新后的models，如果类里没有元素，必须要赋以初值！！！

class Stata(models.Model):
    UserName=models.CharField(max_length=200,default='张三',null=True)
    temperature_1=models.FloatField(default='18.0',null=True)
    temperature_2=models.FloatField(default='18.0',null=True)
    temperature_3=models.FloatField(default='18.0',null=True)
    temperature_4=models.FloatField(default='18.0',null=True)
    temperature_5=models.FloatField(default='18.0',null=True)
    temperature_6=models.FloatField(default='18.0',null=True)
    temperature_7=models.FloatField(default='18.0',null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)
    index_1=models.FloatField(default='1.0',null=True)
    index_2=models.FloatField(default='2.0',null=True)
#class Clothes(models.Model):
 #   temperature_1=models.FloatField(default='18.0',null=True)
  #  temperature_2=models.FloatField(default='18.0',null=True)
   # currenttime=models.DateTimeField('time local',null=True)

class Time_1(models.Model):
    UserName=models.CharField(max_length=200,default='张三',null=True)
    temperature_1=models.FloatField(default='18.0',null=True)
    temperature_2=models.FloatField(default='18.0',null=True)
    temperature_3=models.FloatField(default='18.0',null=True)
    temperature_4=models.FloatField(default='18.0',null=True)
    temperature_5=models.FloatField(default='18.0',null=True)
    temperature_6=models.FloatField(default='18.0',null=True)
    temperature_7=models.FloatField(default='18.0',null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)

class Time_2(models.Model):
    UserName=models.CharField(max_length=200,default='张三',null=True)
    temperature_1=models.FloatField(default='18.0',null=True)
    temperature_2=models.FloatField(default='18.0',null=True)
    temperature_3=models.FloatField(default='18.0',null=True)
    temperature_4=models.FloatField(default='18.0',null=True)
    temperature_5=models.FloatField(default='18.0',null=True)
    temperature_6=models.FloatField(default='18.0',null=True)
    temperature_7=models.FloatField(default='18.0',null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)

class Time_3(models.Model):
    UserName=models.CharField(max_length=200,default='张三',null=True)
    temperature_1=models.FloatField(default='18.0',null=True)
    temperature_2=models.FloatField(default='18.0',null=True)
    temperature_3=models.FloatField(default='18.0',null=True)
    temperature_4=models.FloatField(default='18.0',null=True)
    temperature_5=models.FloatField(default='18.0',null=True)
    temperature_6=models.FloatField(default='18.0',null=True)
    temperature_7=models.FloatField(default='18.0',null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)

class Time_4(models.Model):
    UserName=models.CharField(max_length=200,default='张三',null=True)
    temperature_1=models.FloatField(default='18.0',null=True)
    temperature_2=models.FloatField(default='18.0',null=True)
    temperature_3=models.FloatField(default='18.0',null=True)
    temperature_4=models.FloatField(default='18.0',null=True)
    temperature_5=models.FloatField(default='18.0',null=True)
    temperature_6=models.FloatField(default='18.0',null=True)
    temperature_7=models.FloatField(default='18.0',null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)

class Time_5(models.Model):
    UserName=models.CharField(max_length=200,default='张三',null=True)
    temperature_1=models.FloatField(default='18.0',null=True)
    temperature_2=models.FloatField(default='18.0',null=True)
    temperature_3=models.FloatField(default='18.0',null=True)
    temperature_4=models.FloatField(default='18.0',null=True)
    temperature_5=models.FloatField(default='18.0',null=True)
    temperature_6=models.FloatField(default='18.0',null=True)
    temperature_7=models.FloatField(default='18.0',null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)

class Time_6(models.Model):
    UserName=models.CharField(max_length=200,default='张三',null=True)
    temperature_1=models.FloatField(default='18.0',null=True)
    temperature_2=models.FloatField(default='18.0',null=True)
    temperature_3=models.FloatField(default='18.0',null=True)
    temperature_4=models.FloatField(default='18.0',null=True)
    temperature_5=models.FloatField(default='18.0',null=True)
    temperature_6=models.FloatField(default='18.0',null=True)
    temperature_7=models.FloatField(default='18.0',null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)

class Time_7(models.Model):
    UserName=models.CharField(max_length=200,default='张三',null=True)
    temperature_1=models.FloatField(default='18.0',null=True)
    temperature_2=models.FloatField(default='18.0',null=True)
    temperature_3=models.FloatField(default='18.0',null=True)
    temperature_4=models.FloatField(default='18.0',null=True)
    temperature_5=models.FloatField(default='18.0',null=True)
    temperature_6=models.FloatField(default='18.0',null=True)
    temperature_7=models.FloatField(default='18.0',null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)

class Time_8(models.Model):
    UserName=models.CharField(max_length=200,default='张三',null=True)
    temperature_1=models.FloatField(default='18.0',null=True)
    temperature_2=models.FloatField(default='18.0',null=True)
    temperature_3=models.FloatField(default='18.0',null=True)
    temperature_4=models.FloatField(default='18.0',null=True)
    temperature_5=models.FloatField(default='18.0',null=True)
    temperature_6=models.FloatField(default='18.0',null=True)
    temperature_7=models.FloatField(default='18.0',null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)

class Time_9(models.Model):
    UserName=models.CharField(max_length=200,default='张三',null=True)
    temperature_1=models.FloatField(default='18.0',null=True)
    temperature_2=models.FloatField(default='18.0',null=True)
    temperature_3=models.FloatField(default='18.0',null=True)
    temperature_4=models.FloatField(default='18.0',null=True)
    temperature_5=models.FloatField(default='18.0',null=True)
    temperature_6=models.FloatField(default='18.0',null=True)
    temperature_7=models.FloatField(default='18.0',null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)

class Time_10(models.Model):
    UserName=models.CharField(max_length=200,default='张三',null=True)
    temperature_1=models.FloatField(default='18.0',null=True)
    temperature_2=models.FloatField(default='18.0',null=True)
    temperature_3=models.FloatField(default='18.0',null=True)
    temperature_4=models.FloatField(default='18.0',null=True)
    temperature_5=models.FloatField(default='18.0',null=True)
    temperature_6=models.FloatField(default='18.0',null=True)
    temperature_7=models.FloatField(default='18.0',null=True)
    localtime=models.DateTimeField('date local',default='2020-1-20',null=True)
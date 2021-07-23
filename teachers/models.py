from django.db import models

# Create your models here.

class Teacher(models.Model):

    name=models.CharField(max_length=50) #姓名
    englishname=models.CharField(max_length=50) #拼音
    photo=models.ImageField(upload_to='photos/%Y/%m/%d', blank=True) #照片
    dept=models.CharField(max_length=50) #部门
    organs=models.CharField(max_length=50) #直属机构
    sex=models.CharField(max_length=5) #性别
    rank=models.CharField(max_length=50) #职称
    email=models.CharField(max_length=50) #邮箱
    contact=models.TextField(blank=True) #联系方式
    studyexp=models.TextField(blank=True) #学习经历
    researchfield=models.TextField(blank=True) #研究领域
    papers=models.TextField(blank=True) #论文
    tasks=models.TextField(blank=True) #承担课题
    honors=models.TextField(blank=True) #荣誉
    show=models.BooleanField(default=True) #是否展示

    def __str__(self):
        return self.name

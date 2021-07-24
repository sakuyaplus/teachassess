from django.db import models
from datetime import datetime

# Create your models here.
class TComment(models.Model):
    user_id=models.IntegerField() #评论用户ID
    user_name=models.CharField(max_length=100) #评论用户名
    teacher_id = models.IntegerField() #教师ID
    stars = models.IntegerField() #星数
    message = models.TextField(blank=True) #评论内容
    comment_date = models.DateTimeField(default=datetime.now) #评论日期

    def __str__(self):
        return self.user_id
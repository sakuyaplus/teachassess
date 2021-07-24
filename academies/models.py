from django.db import models

# Create your models here.
class Academy(models.Model):
    
    academy_name=models.CharField(max_length=50) #学院名
  
    def __str__(self):
        return str(self.academy_name)
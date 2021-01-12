from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    age=models.CharField(max_length=20)
    sex=models.CharField(max_length=28)
    bir=models.DateField(auto_now=True,null=True)
    phone=models.CharField(max_length=28)


    class Meta:
        db_table = 'bz_stu'
        verbose_name = '学生表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

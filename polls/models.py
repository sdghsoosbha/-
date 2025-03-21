from django.db import models

# Create your models here.


# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # 定义 __str__ 方法，当打印 Post 对象时，会返回 title 的值。
    def __str__(self):
        return self.choice_text





# Create your models here.


class Post(models.Model):
    # 根据模型自动值数据库中创建一个对应的表，此表包括title, name两个字段
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.title
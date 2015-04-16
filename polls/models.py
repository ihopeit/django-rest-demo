#!coding=utf-8

# Create your models here.
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text


    def __unicode__(self):
        return unicode(self.question_text)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

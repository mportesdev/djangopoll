import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        choices = self.choice_set.all()
        vote_sum = sum(choice.votes for choice in choices)
        return (f'{self.question_text}'
                f' ({len(choices)} options, {vote_sum} votes)')

    def was_published_recently(self):
        now = timezone.now()
        yesterday = now - datetime.timedelta(days=1)
        return yesterday <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

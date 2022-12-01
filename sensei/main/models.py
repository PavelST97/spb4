from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):

    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    is_support = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}'


class Ticket(models.Model):

    STATUSES = [
        ('1', 'NOT SOLVED'),
        ('2', 'SOLVED'),
        ('3', 'FROZEN')
    ]

    owner = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='user')
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='NOT SOLVED', choices=STATUSES)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):

    owner = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='comment_owner')
    to_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name='comment_ticket')
    body = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)




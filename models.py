from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    relation = models.CharField(max_length=100)
    question1 = models.CharField(max_length=255)
    answer1 = models.CharField(max_length=255)
    question2 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    question3 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
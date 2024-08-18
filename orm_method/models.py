from django.db import models
from django.utils import timezone


class Worker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.SmallIntegerField(null=True)
    created = models.DateTimeField(default=timezone.now)
    work_experience = models.SmallIntegerField(default=0)  # хранит значение типа Number, которое представляет небольшое целочисленное значение (от -32768 до 32767).



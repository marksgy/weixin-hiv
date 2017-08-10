from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=128)
    psd = models.CharField(max_length=32)
    qq = models.IntegerField()
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class OrderInfo(models.Model):
    CHECK_CHOICES = (
        ('B', '血检'),
        ('S', '唾检'),
    )
    methods = models.CharField(max_length=2, choices=CHECK_CHOICES)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=11)
    qq = models.IntegerField()
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name
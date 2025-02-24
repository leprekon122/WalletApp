from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PreTag(models.Model):
    objects = None
    pre_tag_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'PreTag'
        verbose_name_plural = 'PreTag'


class WalletTag(models.Model):
    objects = None
    tag_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'WalletTag'
        verbose_name_plural = 'WalletTag'


class WalletData(models.Model):
    objects = None
    price = models.IntegerField()
    wallet_tag = models.ForeignKey(WalletTag, models.CASCADE)
    wallet_pre_tag = models.ForeignKey(PreTag, models.CASCADE)
    date = models.DateField()
    user = models.ForeignKey(User, models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'WalletData'
        verbose_name_plural = 'WalletData'


class NotificationModel(models.Model):
    objects = None
    username = models.ForeignKey(User, models.CASCADE)
    note_text = models.TextField()
    note_date = models.DateField(auto_now=True)
    alarm_date = models.DateField()

    class Meta:
        verbose_name = 'NotificationModel'
        verbose_name_plural = 'NotificationModel'

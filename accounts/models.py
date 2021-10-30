# import instance as instance
# from django.core.serializers import json
# from django.conf import settings
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# #from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# #from utils.common.cipher import AESCiper
# # # #
# # # #
# #
# # # class User(AbstractUser):
# # #     pass
# #
# # class Profile(models.Model):
# #     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 현 계정의 사용자를 가져올 수 있음.
# #     nickname = models.CharField(max_length=64, default='')
# #     major = models.CharField(max_length=200, blank=True)
# #    phone = models.CharField(max_length=200, blank=True)
# # # #
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user_pk = models.IntegerField(blank=True)
#     #email = models.EmailField(max_length=500, blank=True)
#     major = models.CharField(max_length=200, blank=True)
#     point = models.IntegerField(default=0)
#     like = models.CharField(max_length=200, blank=True)
#     phone = models.CharField(max_length=200, blank=True)
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#      if created:
#          Profile.objects.create(user=instance, user_pk=instance.id)
#
# #
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#      instance.profile.save()

# class User(models.Model):
#     class Meta:
#         db_table = "accounts"
#
#     username = models.CharField(max_length=200, primary_key=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_ay = models.DateTimeField(auto_now=True)
#     email = models.CharField(max_length=128, unique=True)
#     password = models.CharField(max_length=225)
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)



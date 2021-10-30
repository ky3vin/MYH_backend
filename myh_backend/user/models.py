from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100, unique=True, null=True)
    mobile_number = models.CharField(max_length=100, unique=True, null=True)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_manager = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    class Meta:
        db_table = 'users'

class Follow(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    following = models.CharField(default='0 ', max_length=5000)
    followedBy = models.CharField(default='0 ', max_length=5000)
    class Meta:
        db_table = 'follows'


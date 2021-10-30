from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

# 공지사항 게시판 몰아보기 기능 : 동아리를 하나의 사용자(User)로 만들어
# 해당 동아리와 following 관계를 맺은 사용자가 동아리에 작성된 게시글을 읽을 수 있도록 함
# 인스타그램에서 팔로잉을 클릭하면 내가 팔로우하는 계정이 나열되는 것 처럼, 동아리들이 나열됨


class Following(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # 나를 구독하는 유저
    follower=models.OneToOneField(User, related_name='follower', on_delete=models.CASCADE)
    # 내가 구독하는 유저 (가입한 동아리)
    follow=models.ManyToManyField(User, related_name='follow')

    class Meta:
        abstract = True


class Posting(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    post_title = models.TextField(blank=True)
    post_text = models.TextField(blank=True)
    post_created = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "text : "+self.post_title

    class Meta:
        ordering = ['-post_created']


    def get_absolute_url(self):
        return reverse('noticeBoard:detail', args=[self.id])


class Club(models.Model):
    club_title = models.TextField(blank=True)
    club_text = models.TextField(blank=True)
    is_member = models.BooleanField(default=False)
    def __str__(self):
        return self.club_title

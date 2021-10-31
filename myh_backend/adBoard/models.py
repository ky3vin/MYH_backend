from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

club_category = (
    ('공연', '공연'),
    ('레저', '레저'),
    ('전시', '전시'),
    ('사회', '사회'),
    ('스포츠', '스포츠'),
    ('종교', '종교'),
    ('학술', '학술'),
)


class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to= 'timeline_photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    on_going = models.BooleanField(default=True) #모집중
    keep_going = models.BooleanField(default=False) #상시모집
    due_date = models.TextField(blank=True)
    #updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=20, choices=club_category, default='일반')
    club_name = models.TextField(blank=True)

    def __str__(self):
        return "text : "+self.text

    class Meta:
        ordering = ['-created']


    def get_absolute_url(self):
        return reverse('adBoard:detail', args=[self.id])


class Apply(models.Model):
    #applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applicant')
    applicant = models.TextField(blank=False)
    apply_text = models.TextField(blank=True)
    apply_created = models.DateTimeField(auto_now_add=True)
    apply_club_name = models.TextField(blank=True)

    def __str__(self):
        return self.apply_text

    class Meta:
        ordering = ['-apply_created']

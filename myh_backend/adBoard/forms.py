from django import forms
from .models import Apply


class ApplyForm(forms.ModelForm):

    class Meta:
        model = Apply
        fields = ['applicant', 'apply_club_name', 'apply_text']
from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name=forms.CharField(label='your name',max_length=20)
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
        labels={
            'user_name':'your name',
            'rating':'your rating',
            'review_text':'your feedback'
        }
from django import forms
from django.forms import ModelForm, Textarea
from reviews.models import Wine, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }

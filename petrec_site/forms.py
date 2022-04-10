from django import forms
from .models import Feedback

class uploadFile(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = []

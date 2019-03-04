from django import forms
from .models import foodfitnessModel

class foodfitnessForm(forms.ModelForm):
    class Meta:
        model=foodfitnessModel
        fields=['username','calories','date']
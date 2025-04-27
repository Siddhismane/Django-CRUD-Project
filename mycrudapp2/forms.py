from django import forms
from .models import Intern

class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = ['name', 'email', 'phone']

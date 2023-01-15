from django import forms
from django.forms import ModelForm
from .models import Tugas

class TugasForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task ...'}))

    class Meta:
        model = Tugas
        fields = "__all__"
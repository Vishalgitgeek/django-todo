from django import forms
from django.forms import ModelForm

from .models import Task
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'complete']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Add new task...'}),
            'complete': forms.CheckboxInput(),
        }
        labels = {
            'title': '',
            'complete': 'Completed',
        }
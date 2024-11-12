from django import forms
from .models import Model

class ModelsForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = '__all__'
        widgets  = {
            'task_assign_date' : forms.NumberInput(attrs={'type': 'date'}),
        }
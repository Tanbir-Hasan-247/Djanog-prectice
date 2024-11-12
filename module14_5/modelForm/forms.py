from django import forms
 
from .models import GeeksModel
 
class ModelForm(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = "__all__"

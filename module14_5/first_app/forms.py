from django import forms
import datetime
from django.forms.widgets import NumberInput

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
class ExampleForm(forms.Form):
    name = forms.CharField(initial='Enter your Name...')
    comment = forms.CharField(widget= forms.Textarea(attrs={'rows':2}))
    email = forms.EmailField(label='Enter your Email...')
    check = forms.BooleanField(initial=True)
    date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    email_address = forms.EmailField(required=False)
    day = forms.DateField(initial=datetime.date.today)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect , choices=FAVORITE_COLORS_CHOICES)
    favorite_color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple , choices=FAVORITE_COLORS_CHOICES)

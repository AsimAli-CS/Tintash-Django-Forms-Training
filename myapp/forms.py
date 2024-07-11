# myapp/forms.py
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_age = forms.IntegerField(label='Your age')  # Add age fields
   


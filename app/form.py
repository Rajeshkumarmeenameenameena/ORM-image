from django import forms
from .models import *
from django.forms import ModelForm
# class studentform(forms.Form):
#     name=forms.CharField(max_length=20,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
#     email=forms.EmailField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
#     phoneno=forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))

class studentform(forms.ModelForm):
    class Meta: 
        model=student
        fields= '__all__'
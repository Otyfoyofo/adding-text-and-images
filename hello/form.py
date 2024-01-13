from django import forms

class Postforms(forms.Form):
    image=forms.FileField()
    text=forms.CharField()
    text=forms.CharField(label='Description')
    

from django import forms
from .models import Task
from .models import Cumples



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Escriba un titulo'}),
             'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Escriba una descripcion'}),
              'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }
        

    
class CumpleForm(forms.ModelForm):
    class Meta:
        model = Cumples
        fields = ['fecha', 'description']
        widgets = {
             'fecha': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Escriba un titulo'}),
             'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Cumpleañero'}),
              
        }
        
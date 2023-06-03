from django import forms
from .models import Task
from .models import Cumple



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Escriba un titulo'}),
             'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Escriba una descripcion'}),
              'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }
        

    
#class CumpleForm(forms.ModelForm):
    #class Meta:
        #model = Cumple
        #fields = ['fecha', 'description']
        #widgets = {
            # 'fecha': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Escriba un titulo'}),
             #'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Cumpleañero'}),
              
        #}



class CumpleForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'Fecha', 'class': 'form-control'}),
        help_text='Formato: DD/MM/AAAA'
    )
    descripcion = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Cumpleañero', 'class': 'form-control'}),
        
    )

    class Meta:
        model = Cumple
        fields = ('fecha', 'descripcion')

        
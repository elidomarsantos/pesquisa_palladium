from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import Pesquisa

class DateInput(forms.DateInput):
    input_type = 'date'
    



class Form_Pesquisa(forms.ModelForm):
    
    class Meta:
        model = Pesquisa
        fields = '__all__'
        widgets = {
          'compromissos': forms.Textarea(attrs={'rows':4}),
          'pontos_reforçar': forms.Textarea(attrs={'rows':4}),
          'pontos_fortes': forms.Textarea(attrs={'rows':4}),
          'justificativa01': forms.Textarea(attrs={'rows':3}),
          'justificativa02': forms.Textarea(attrs={'rows':3}),
          'justificativa03': forms.Textarea(attrs={'rows':3}),
          'justificativa04': forms.Textarea(attrs={'rows':3}),
          'justificativa05': forms.Textarea(attrs={'rows':3}),
          'justificativa06': forms.Textarea(attrs={'rows':3}),
          'justificativa07': forms.Textarea(attrs={'rows':3}),
          'justificativa08': forms.Textarea(attrs={'rows':3}),
          'justificativa09': forms.Textarea(attrs={'rows':3}),
          'justificativa10': forms.Textarea(attrs={'rows':3}),
        }
        
       

   
        
        
         


              
          


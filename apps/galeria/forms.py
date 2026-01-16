from django import forms

from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada',]

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Fotografia'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Legenda da Fotografia'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descritao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição da Fotografia'}),
            'foto': forms.FileInput(attrs={'class': 'form-control-file'}),
            'data_fotografia': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                    }
            ),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }
        
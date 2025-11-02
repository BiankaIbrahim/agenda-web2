from django import forms
from .models import Contato, Lembrete

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'observacoes']

# Formulário para registrar lembretes
class LembreteForm(forms.ModelForm):
    class Meta:
        model = Lembrete
        fields = ['contato', 'titulo', 'descricao', 'data_hora']
        # Pode adicionar widgets ou outros campos aqui, se desejar
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
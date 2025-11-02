from django import forms
from .models import Usuario

# Formulário para criar e editar um usuário (substituiria o 'UserCreationForm' do Django)
class UsuarioForm(forms.ModelForm):
    # O campo 'senha' deve usar um widget de PasswordInput para ocultar a entrada
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        # 'senha' deve ser incluída para o cadastro
        fields = ['nome', 'email', 'senha'] 

# Formulário de login simples (não baseado em modelo)
class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    # O campo 'senha' deve usar um widget de PasswordInput para ocultar a entrada
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
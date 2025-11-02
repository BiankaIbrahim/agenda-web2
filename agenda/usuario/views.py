from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Usuario
from .forms import LoginForm, UsuarioForm

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            novo_usuario = form.save(commit=False)
            novo_usuario.save()
            
            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login_usuario') 
    else:
        form = UsuarioForm()
    return render(request, 'usuario/cadastro.html', {'form': form})


def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            
            try:
                usuario = Usuario.objects.get(email=email)
                
                if usuario.senha == senha: 
                    request.session['usuario_id'] = usuario.id
                    messages.success(request, f'Bem-vindo, {usuario.nome}!')
                    return redirect('lista_contatos') 
                else:
                    messages.error(request, 'Email ou senha inválidos.')
            except Usuario.DoesNotExist:
                messages.error(request, 'Email ou senha inválidos.')
    else:
        form = LoginForm()
        
    return render(request, 'usuario/login.html', {'form': form})


@login_required 
def editar_perfil(request):
    # Obtém o usuário logado
    usuario_id = request.session.get('usuario_id')
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('lista_contatos') 
    else:
        form = UsuarioForm(instance=usuario)
        del form.fields['senha'] 
        
    return render(request, 'usuario/editar_perfil.html', {'form': form})

def logout_usuario(request):
    if 'usuario_id' in request.session:
        del request.session['usuario_id']
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('login_usuario')

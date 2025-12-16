from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Usuario
from .forms import LoginForm, UsuarioForm
from .decorators import usuario_logado

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_senha(form.cleaned_data['senha'])
            usuario.save()

            messages.success(request, 'Cadastro realizado com sucesso!')
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

                if usuario.check_senha(senha):
                    request.session['usuario_id'] = usuario.id
                    request.session.set_expiry(3600) 

                    messages.success(request, f'Bem-vindo, {usuario.nome}!')
                    return redirect('lista_contatos')
                else:
                    messages.error(request, 'Email ou senha inválidos.')
            except Usuario.DoesNotExist:
                messages.error(request, 'Email ou senha inválidos.')
    else:
        form = LoginForm()

    return render(request, 'usuario/login.html', {'form': form})

@usuario_logado
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
        
    return render(request, 'usuario/editar.html', {'form': form})

def logout_usuario(request):
    request.session.flush()
    messages.info(request, 'Logout realizado com sucesso.')
    return redirect('login_usuario')

def visualizar_perfil(request):
    usuario_id = request.session.get('usuario_id')
    
    if not usuario_id:
        messages.warning(request, 'Você precisa estar logado para ver o perfil.')
        return redirect('login_usuario')
        
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    return render(request, 'usuario/perfil.html', {'usuario': usuario})
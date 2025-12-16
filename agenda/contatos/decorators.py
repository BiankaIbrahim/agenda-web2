from django.shortcuts import redirect
from django.contrib import messages

def contato_logado(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('usuario_id'):
            messages.warning(request, 'Você precisa estar logado para acessar a agenda.')
            return redirect('login_usuario')
        return view_func(request, *args, **kwargs)
    return wrapper

from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import Contato
from .forms import ContatoForm
from .forms import LembreteForm # Certifique-se que você tem este import!
from .models import Contato, Lembrete 
from django.conf import settings 

def lista_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/lista.html', {'contatos': contatos})


NOTIFICACAO_URL = getattr(settings, "NOTIFY_URL", None)  # definir em settings.py

def criar_contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save()

            # chamar Lambda via API Gateway
            if NOTIFICACAO_URL:
                try:
                    payload = {"nome": contato.nome, "email": contato.email}
                    headers = {'Content-Type': 'application/json'}
                    requests.post(NOTIFICACAO_URL, json=payload, headers=headers, timeout=3)
                except Exception as e:
                    print("Erro ao notificar Lambda:", e)
           
            return redirect('lista_contatos')
    else:
        form = ContatoForm()
    return render(request, 'contatos/form.html', {'form': form})

def editar_contato(request, id):
    contato = get_object_or_404(Contato, id=id)
    if request.method == 'POST':
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect('lista_contatos')
    else:
        form = ContatoForm(instance=contato)
    return render(request, 'contatos/form.html', {'form': form})

def deletar_contato(request, id):
    contato = get_object_or_404(Contato, id=id)
    contato.delete()
    return redirect('lista_contatos')

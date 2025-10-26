from django.urls import path
from . import views  # Importa o módulo de views do app contatos

urlpatterns = [
    path('', views.lista_contatos, name='lista_contatos'),            # Lista todos os contatos
    path('novo/', views.criar_contato, name='criar_contato'),         # Cria novo contato
    path('editar/<int:id>/', views.editar_contato, name='editar_contato'),  # Edita contato existente
    path('deletar/<int:id>/', views.deletar_contato, name='deletar_contato'),  # Deleta contato
]
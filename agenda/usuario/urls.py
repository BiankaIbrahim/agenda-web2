from django.urls import path
from . import views  

urlpatterns = [
    path('cadastro/', views.criar_usuario, name='criar_usuario'),        
    path('', views.login_usuario, name='login_usuario'),  
    path('perfil/', views.visualizar_perfil, name='visualizar_perfil'),        
    path('perfil/editar/', views.editar_perfil , name='editar_perfil'),     
    path('logout/', views.logout_usuario, name='logout_usuario'),           
]
from django.urls import path
from . import views  

urlpatterns = [
    path('cadastro/', views.criar_usuario, name='criar_usuario'),        
    path('', views.login_usuario, name='login_usuario'),             
    path('editar/', views.editar_perfil, name='editar_perfil'),     
    path('logout/', views.logout_usuario, name='logout_usuario'),           
]
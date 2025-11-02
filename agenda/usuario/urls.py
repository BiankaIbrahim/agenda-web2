from django.urls import path
from . import views  

urlpatterns = [
    path('', views.criar_usuario, name='criar_usuario'),        
    path('login/', views.login_usuario, name='login_usuario'),             
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),     
    path('logout/', views.logout_usuario, name='logout_usuario'),           
]
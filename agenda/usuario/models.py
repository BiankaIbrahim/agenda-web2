from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    def set_senha(self, senha_plana):
        self.senha = make_password(senha_plana)

    def check_senha(self, senha_plana):
        return check_password(senha_plana, self.senha)

    def __str__(self):
        return self.nome

from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    observacoes = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Lembrete(models.Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE, related_name='lembretes')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    data_hora = models.DateTimeField()
    enviado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo} - {self.contato.nome}"
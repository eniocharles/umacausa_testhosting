from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = (
        (1, 'Usuário Comum'),
        (2, 'Instituição')
    )

    id_usuario = models.AutoField(primary_key=True, null=False)
    nome = models.TextField(null=False)
    nome_usuario = models.TextField(null=False)
    cpf = models.TextField(null=True)
    email = models.EmailField(null=False)
    telefone = models.TextField(null=False)
    tipo_usuario = models.IntegerField(null=False, choices=TIPO_USUARIO_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

from django.db import models

# Create your models here.

class Conta(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50, default='NÃO INFORMAR', choices=(
        ('NÃO INFORMAR', 'Não Informar'),
        ('MASCULINO', 'Masculino'),
        ('FEMININO', 'Feminino'),
    ))
    email = models.EmailField()
    data_de_nascimento = models.DateTimeField()
    portador_de_deficiencia = models.BooleanField(default=False)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='contas/')
from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=20)

    def __str__ (self):
        return self.nome

# Crie seus modelos aqui.
class Funcionario (models.Model):

    CARGO = [
        ('ES', 'Estágiario'),
        ('AS', 'Assistente'),
        ('JR', 'Junior'),
        ('PL', 'Pleno'),
        ('SR', 'Sênior'),
        ('GR', 'Gerente')        
    ]

    matricula = models.IntegerField()
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=30, choices=CARGO)
    departamento =models.ForeignKey(Departamento, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_nascimento = models.DateField(null=True)

    class Meta():
        ordering = ['nome']

    def __str__ (self):
        return self.nome
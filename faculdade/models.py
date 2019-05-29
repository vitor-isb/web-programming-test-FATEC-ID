from django.db import models
from django.utils import timezone
# Create your models here.
class Professor(models.Model):
    nfunc = models.IntegerField()
    nome = models.CharField(max_length=100)
    end = models.CharField(max_length=200)
    titulacao = models.CharField(max_length=50)
    fone = models.CharField(max_length=13)
    def salvar(self):
        self.save()

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    codigo = models.IntegerField()
    titulo = models.CharField(max_length=25)
    def __str__(self):
        return self.titulo

class Aluno(models.Model):
    nummat = models.IntegerField()
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Matricula(models.Model):
    nummat = models.ForeignKey(Aluno,on_delete=models.CASCADE)
    codigo = models.ForeignKey(Disciplina,on_delete=models.CASCADE)
    ano = models.IntegerField()
    faltas = models.IntegerField()
    nota_final = models.IntegerField() 
    def __str__(self):
        return self.nummat

class Alocacao(models.Model):
    nfunc = models.ForeignKey(Professor,on_delete=models.CASCADE)
    codigo = models.ForeignKey(Disciplina,on_delete=models.CASCADE)
    horario = models.TimeField()
    carga = models.IntegerField()
    #def __str__(self):
        
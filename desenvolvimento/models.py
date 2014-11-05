from django.db import models

# Create your models here.

class DepartamentoAcademico(models.Model):
        nome = models.CharField('Nome', max_length=100)
        sigla = models.CharField('Sigla', max_length=100)
        #chefe = models.ForeignKey(Professor)
        #suplente = models.ForeignKey(Professor)
        #funcionario = [Funcionario]


class Funcionario(models.Model):
	nome = models.CharField('Nome', max_length=100)
	email = models.CharField('E-mail', max_length=200)
	telefone = models.CharField('Telefone', max_length=20)
	departamento = models.ForeignKey(DepartamentoAcademico)
	funcao = models.CharField('Funcao', max_length=100)

class Professor(Funcionario, models.Model):
	lattes = models.CharField('Link do Lattes', max_length=50)
	#foto

class Curso(models.Model):
        nome = models.CharField('Curso',max_length=50)
        sigla = models.CharField('Sigla', max_length=20)
        disciplina = models.CharField('Disciplina', max_length=100)

class Coordenacao(models.Model):
	coordenador = models.ForeignKey(Professor, related_name = 'coordenadorCoo')
	suplente = models.ForeignKey(Professor, related_name = 'suplenteCoo')
	curso = models.ForeignKey(Curso)

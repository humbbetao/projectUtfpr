import os

from django.db import models
from django.db.models import ImageField

from projectUtfpr.settings import MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATIC_URL


class DepartamentoAcademico(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sigla = models.CharField('Sigla', max_length=100)

    def __unicode__(self):
        return self.nome

# class Pessoa(models.Model):
#     nome = models.CharField('Nome', max_length=100)

# class Professor (Pessoa):

# def get_image_path(instance, filename):
#     return os.path.join('home/humberto/Documentos/projectUtfpr/desenvolvimento/static/img/profilePhoto', str(instance.id), filename)

class Professor(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.CharField('E-mail', max_length=200, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=20, null=True, blank=True)
    departamento = models.ForeignKey(DepartamentoAcademico)
    funcao = models.CharField('Funcao', max_length=100)
    lattes = models.CharField('Link do Lattes', max_length=50, null=True, blank=True)
    bolsaprodutividade = models.CharField('Bolsa Produtividade', max_length=100, null=True, blank=True)
    enderecoprofissional = models.CharField('Endereco Profissional', max_length=5000, null=True, blank=True)
    nomeemcitacoesbibliograficas = models.CharField('Nome em Citacoes Bibliograficas', max_length=255, null=True, blank=True)
    textoResumo = models.CharField('bolsaProdutividade', max_length=500, null=True, blank=True)
    profile_image = ImageField(upload_to="", blank=True, null=True)

    def __unicode__(self):
        return self.nome

# class DadosDePessoa(models.Model):

class DadosDeProfessor(models.Model):
    nome = models.CharField('nome do professor', max_length=100)
    professorDados =  models.ForeignKey(Professor, related_name='DadosDeProfessor')



class Formacao(models.Model):
    ano_inicio = models.CharField('Ano de Inicio', max_length=4)
    ano_conclusao = models.CharField('Ano de Conclusao', max_length=4)
    tipo = models.CharField('Tipo', max_length=511)
    descricao = models.CharField('Descricao', max_length=5000)
    nome = models.CharField('Nome', max_length=5000)
    formacaoProfessor = models.ForeignKey(Professor, related_name='FormacaoProfessor')
    def __unicode__(self):
        return self.nome

class AreaDeAtuacao(models.Model):
    descricao = models.CharField('Area de Atuacao', max_length=511)
    areaProfessor = models.ForeignKey(Professor, related_name='AreaProfessor')
    def __unicode__(self):
        return self.descricao



class Curso(models.Model):
    nome = models.CharField('Curso', max_length=50)
    sigla = models.CharField('Sigla', max_length=20, null=True, blank=True)
    departamentoAcademico = models.ForeignKey(DepartamentoAcademico, related_name="DepartamentoAcademico")
    cargaHoraria =  models.CharField('CargaHoraria', max_length=20, null=True, blank=True)
    estagio =  models.CharField('Estagio',  max_length=256, null=True, blank=True)
    atividadeComplementar = models.CharField('Atividade Complementar', max_length=256, null=True, blank=True)
    optativasDoCurso = models.CharField('OptativasDoCurso', max_length=256, null= True, blank=True)


class Disciplinas(models.Model):
    nome = models.CharField('Nome da Disciplina', max_length=50)
    sigla = models.CharField('Sigla da Disciplina', max_length=50)
    ementa = models.CharField('Ementa', max_length=50)
    descricao = models.CharField('Descricao', max_length=50)
    cargaHoraria= models.CharField('Carga Horaria', max_length=50)

    OptativaHumanas = 'OH'
    OptativaProfissionalizante  = 'OP'
    NucleoComum = 'NC'
    FormacaoProfissionalizante = 'FP'
    TIPODEDISCIPLINA = (
        (OptativaHumanas, 'Optativa Humanas'),
        (OptativaProfissionalizante, 'Optativa Profissionalizante'),
        (NucleoComum, 'Nucleo Comum'),
        (FormacaoProfissionalizante, 'Formacao Profissionalizante'),
    )
    tipo  = models.CharField(max_length=2,
                                      choices=TIPODEDISCIPLINA,
                                      default=FormacaoProfissionalizante)
    cursoNome= models.ForeignKey(Curso, related_name="CursoNome")

    #carga horaria
    #de aula, estagio, atividade complementar, optativas

    #modelar cursos
    #add disciplinas
    #disciplina: nome, sigla, periodo, ementa, descricao, carga horaria, tipo





class Coordenacao(models.Model):
    coordenador = models.ForeignKey(Professor, related_name='coordenadorCoo')
    suplente = models.ForeignKey(Professor, related_name='suplenteCoo')
    curso = models.ForeignKey(Curso,related_name='Curso' )


class Artigo(models.Model):
    listadeautores = models.CharField('Lista de Autores', max_length=5000)
    titulo = models.CharField('Titulo do Artigo', max_length=255)
    data = models.CharField('Data do Artigo', max_length=5)
    doi = models.CharField('DOI', max_length=255, null=True, blank=True)
    paginas = models.CharField('Paginas', max_length=10, null=True, blank=True)
    resumo = models.CharField('Resumo', max_length=5000)

    professores= models.ManyToManyField(Professor,related_name="ArtigoProfessor");


    def __unicode__(self):
        return self.titulo




class ArtigoEmPeriodico(Artigo):
    nomejournal = models.CharField('Nome Journal', max_length=255)
    ISSN = models.CharField('Codigo ISSN', max_length=255)
    publisher = models.CharField('Editora', max_length=255)
    numero = models.CharField('Numero', max_length=100)
    volume = models.CharField('Volume', max_length=100)


    def __unicode__(self):
        return self.titulo

class ArtigoEmConferencia(Artigo):
    nomedaConferencia = models.CharField('Nome da Conferencia', max_length=255)
    ISSN = models.CharField('Codigo ISSN', max_length=50)
    ISBN = models.CharField('Codigo ISBN', max_length=50)  # obrigatorio
    local = models.CharField('Local da Conferencia', max_length=255)
    ano = models.CharField('Ano', max_length=4)

class Integrante(models.Model):
    nome = models.CharField('nome', max_length=255)
    ehCoordenador = models.BooleanField(default=False)
    def __unicode__(self):
        return self.nome

class IntegranteProfessor(Integrante):
    professor=  models.ForeignKey(Professor, related_name='ProfessorIntegrante')

class Projeto(models.Model):
    datainicio = models.CharField('Data Inicio', max_length=5, null=True, blank=True)
    datadefim = models.CharField('Data de Fim', max_length=5, null=True, blank=True)
    agendafinanciadora = models.CharField('Agencia Financiadora', max_length=255, null=True, blank=True)
    nome = models.CharField('Nome do Projeto', max_length=1000)
    resumo = models.CharField('Resumo', max_length=10000)
    situacao = models.CharField('Situacao', max_length=100, null=True, blank=True)
    natureza = models.CharField('Natureza', max_length=100, null=True, blank=True)
    professor = models.ForeignKey(Professor, related_name='Professor')

    def __unicode__(self):
        return self.nome



class Evento(models.Model):
    doi = models.CharField('DOI', max_length=255)
    autores = models.CharField('Autores', max_length=5000)
    titulo = models.CharField('Titulo', max_length=5000)
    nomeevento = models.CharField('Nome do Evento', max_length=5000, null=True, blank=True)
    ano = models.CharField('Ano', max_length=4)
    volume = models.CharField('Volume', max_length=10)
    paginas = models.CharField('Paginas', max_length=255)

    def __unicode__(self):
        return self.titulo
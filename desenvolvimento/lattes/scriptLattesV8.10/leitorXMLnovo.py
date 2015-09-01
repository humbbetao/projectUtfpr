#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from string import split
from subprocess import call
import subprocess
import xml.etree.cElementTree as et
import csv
import sys
import mysql.connector
import sys
import shutil
# import Levenshtein
import os, errno
import warnings

warnings.filterwarnings('ignore')

sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/producoesBibliograficas/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/producoesTecnicas/')
sys.path.append('desenvolvimen'
                'to/lattes/scriptLattesV8.10/scriptLattes/producoesArtisticas/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/producoesUnitarias/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/orientacoes/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/eventos/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/charts/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/internacionalizacao/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/qualis/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/patentesRegistros/')


class Departamento(object):
    nome, sigla = "", ""

    def __init__(self):
        self.nome = ""
        self.sigla = ""


class Professor(object):
    nome, email, telefone, departamento, funcao, \
    lattes, bolsaProdutividade, enderecoProfissional, \
    nomeEmCitacoesBibliograficas, textoResumo, enderecoProfissional_lat, enderecoProfissional_long = "", "", "", "", "", "", "", "", "", "", "", ""

    def __init__(self):
        self.nome = ""
        self.email = ""
        self.telefone = ""
        self.departamento = None
        self.funcao = ""
        self.lattes = ""
        self.bolsaProdutividade = ""
        self.enderecoProfissional = ""
        self.nomeEmCitacoesBibliograficas = ""
        self.textoResumo = ""


class Formacao(object):
    anoInicio, anoConclusao, tipo, descricao = "", "", "", ""

    def __init__(self):
        self.anoInicio = ""
        self.anoConclusao = ""
        self.tipo = ""
        self.descricao = ""


class AreaDeAtuacao(object):
    descricao = ""

    def __index__(self):
        self.descricao = ""


class Curso(object):
    nome, sigla = "", ""

    def __init__(self):
        self.nome = ""
        self.sigla = ""


class Coordenacao(object):
    coordenador, suplente, curso = "", "", ""

    def __init__(self):
        self.coordenador = ""
        self.suplente = ""
        self.curso = ""


class Artigo(object):
    listaDeAutores, titulo, data, doi, paginas, resumo = "", "", "", "", "", ""

    def __init__(self):
        self.data = ""
        self.doi = ""
        self.listaDeAutores = ""
        self.paginas = ""
        self.resumo = ""
        self.titulo = ""


class ArtigoEmPeriodico(Artigo):
    nomeJournal, ISSN, publisher, numero, volume = "", "", "", "", ""

    def __init__(self):
        self.titulo = "",
        self.resumo = ""
        self.paginas = "",
        self.listaDeAutores = ""
        self.data = ""
        self.doi = ""
        self.ISSN = ""
        self.nomeJournal = ""
        self.numero = ""
        self.publisher = ""


class ArtigoEmConferencia(Artigo):
    nomedaConferencia, ISSN, ISBN, local = "", "", "", ""

    def __init__(self):
        self.titulo = ""
        self.ISSN = ""
        self.data = ""
        self.doi = ""
        self.listaDeAutores = ""
        self.ISBN = ""
        self.local = ""
        self.paginas = ""
        self.nomedaConferencia = ""
        self.resumo = ""


class Projeto(object):
    listadeCoordenadores, listaColaboradores, dataInicio, datadeFim, \
    AgendaFinanciadora, nome, resumo = "", "", "", "", "", "", ""

    def __init__(self):
        self.listaColaboradores = ""
        self.resumo = ""
        self.AgendaFinanciadora = ""
        self.datadeFim = ""
        self.dataInicio = ""
        self.nome = ""
        self.resumo = ""


class Evento(object):
    doi, autores, titulo, nomeEvento, ano, volume, paginas = "", "", "", "", "", "", ""

    def __init__(self):
        self    .doi = ""
        self.autores = ""
        self.titulo = ""
        self.nomeEvento = ""
        self.ano = ""
        self.volume = ""
        self.paginas = ""


def utfpr():
    print("Deu Certo")
    return None


def executeLattes():
    call("python scriptLattes.py ./data/scriptlattes-utfpr-cm-dacom.config", shell=True)


def executeLeitorXML():
    # fd = open("data/lattes-site/database.xml")
    # parsedXML = et.parse(fd)
    # curriculo_lattes = parsedXML.findall("pesquisador")
    # definindo Arrays
    professor = []
    arraysProfNovo = []
    projetoPesquisa = []
    artigos = []
    artigosEmPeriodico = []
    artigosEmConferencia = []
    tree = et.parse("data/lattes-site/database.xml")
    root = tree.getroot()

    for child in root:
        prof = Professor()
        print(child.tag, child.attrib, "//////1")
        prof.lattes = child.get('id')
        print(prof.lattes)
        for child1 in child:
            # print(grand.tag, grand.attrib, "/////2")
            for identificacao in child1.iter('identificacao'):
                if identificacao.find('nome_inicial').text is not None:
                    nome_inicial = identificacao.find('nome_inicial').text
                if identificacao.find('nome_completo').text is not None:
                    nome_completo = identificacao.find('nome_completo').text
                if identificacao.find('nome_citacao_bibliografica').text is not None:
                    nome_citacao_bibliografica = identificacao.find('nome_citacao_bibliografica').text
                if identificacao.find('sexo').text is not None:
                    sexo = identificacao.find('sexo').text

                prof.nome = nome_inicial
                prof.nome_completo = nome_completo
                prof.nomeEmCitacoesBibliograficas = nome_citacao_bibliografica
                prof.sexo = sexo
                prof.departamento = 1
                prof.funcao = "Professor"

                professor.append(prof)

            for endereco in child1.iter('endereco'):
                if endereco.find('endereco_profissional').text is not None:
                    endereco_profissional = endereco.find('endereco_profissional').text
                if endereco.find('endereco_profissional_lat').text is not None:
                    endereco_profissional_lat = endereco.find('endereco_profissional_lat').text
                if endereco.find('endereco_profissional_long').text is not None:
                    endereco_profissional_long = endereco.find('endereco_profissional_long').text

            for formacao in child1.iter('formacao_academica'):
                for formacao1 in formacao.iter('formacao'):
                    if formacao1.find('ano_inicio').text is not None:
                        ano_inicio = formacao1.find('ano_inicio').text
                    if formacao1.find('ano_conclusao').text is not None:
                        ano_conclusao = formacao1.find('ano_conclusao').text
                    if formacao1.find('tipo').text is not None:
                        tipo = formacao1.find('tipo').text
                    if formacao1.find('nome_instituicao').text is not None:
                        nome = formacao1.find('nome_instituicao').text
                    if formacao1.find('descricao').text is not None:
                        descricao = formacao1.find('descricao').text
            for projetospesquisa in child1.iter('projetos_pesquisa'):
                for projeto in projetospesquisa.iter('projeto'):

                    if projeto.find('ano_inicio').text is not None:
                        ano_inicio = projeto.find('ano_inicio').text
                    if projeto.find('ano_conclusao').text is not None:
                        ano_conclusao = projeto.find('ano_conclusao').text
                    if projeto.find('nome').text is not None:
                        nome = projeto.find('nome').text
                    if projeto.find('descricao').text is not None:
                        descricao = projeto.find('descricao').text

                    projeto = Projeto()
                    projeto.dataInicio = ano_inicio
                    projeto.datadeFim = ano_conclusao
                    projeto.nome = nome
                    projeto.resumo = descricao

                    projetoPesquisa.append(projeto)

            for areaatuacao in child1.iter('area_atuacao'):
                descricao = areaatuacao.find('descricao').text
                print(descricao)

            for eventos in child1.iter('trabalho_completo_congresso'):  # eventos
                for evento in eventos.iter('trabalho_completo'):
                    if evento.find('doi').text is not None:
                        doi = evento.find('doi').text
                    if evento.find('autores').text is not None:
                        autores = evento.find('autores').text
                    if evento.find('titulo').text is not None:
                        titulo = evento.find('titulo').text
                    if evento.find('nome_evento').text is not None:
                        nome_evento = evento.find('nome_evento').text
                    if evento.find('ano').text is not None:
                        ano = evento.find('ano').text
                    if evento.find('volume').text is not None:
                        volume = evento.find('volume').text
                    if evento.find('paginas').text is not None:
                        paginas = evento.find('paginas').text
            for resumoCongresso in child1.iter('resumo_congresso'):
                for resumCo in resumoCongresso.iter('resumo'):
                    if resumCo.find('doi').text is not None:
                        doi = resumCo.find('doi').text
                    if resumCo.find('autores').text is not None:
                        autores = resumCo.find('autores').text
                    if resumCo.find('titulo').text is not None:
                        titulo = resumCo.find('titulo').text
                    if resumCo.find('nome_evento').text is not None:
                        nome_evento = resumCo.find('nome_evento').text
                    if resumCo.find('ano').text is not None:
                        ano = resumCo.find('ano').text
                    if resumCo.find('volume').text is not None:
                        volume = resumCo.find('volume').text
                    if resumCo.find('paginas').text is not None:
                        paginas = resumCo.find('paginas').text
                    if resumCo.find('numero').text is not None:
                        numero = resumCo.find('numero').text
            for artigoPeriodico in child1.iter('artigos_em_periodicos'):
                for artigo in artigoPeriodico.iter('artigo'):
                    if artigo.find('doi').text is not None:
                        doi = artigo.find('doi').text
                    if artigo.find('autores').text is not None:
                        autores = artigo.find('autores').text
                    if artigo.find('titulo').text is not None:
                        titulo = artigo.find('titulo').text
                    if artigo.find('revista').text is not None:
                        revista = artigo.find('revista').text
                    if artigo.find('ano').text is not None:
                        ano = artigo.find('ano').text
                    if artigo.find('volume').text is not None:
                        volume = artigo.find('volume').text
                    if artigo.find('paginas').text is not None:
                        paginas = artigo.find('paginas').text
                    if artigo.find('numero').text is not None:
                        numero = artigo.find('numero').text




                        # Aqui
                        # Insercao No BD

                        # abrindoCOnexao

    config = {
        'user': 'root',
        'passwd': 'root',
        'database': 'UTFPR'
    }
    connection = mysql.connector.connect(**config)
    conector = connection.cursor()
    profs = []
    # auxiliar=0
    conector.execute("SELECT * FROM desenvolvimento_professor")
    resultProfessor = conector.fetchall()

    conector.execute("SELECT * FROM desenvolvimento_artigo")
    resultArtigo = conector.fetchall()

    conector.execute ("SELECT * FROM desenvolvimento_artigoemconferencia")
    resultAritgoEmConferencia = conector.fetchall()

    conector.execute ("SELECT * FROM desenvolvimento_artigoemperiodico")
    resultArtigoEmPeriodico = conector.fetchall()

    conector.execute ("SELECT * FROM desenvolvimento_formacao")
    resultFormacao = conector.fetchall()

    conector.execute ("SELECT * FROM desenvolvimento_projeto")
    resultProjeto = conector.fetchall()




    # inverter as ordem dos for
    # colocar o q ta fora dentro e q ta dentro fora

    arraysProfNovo =[]
    auxil = 0

    #     # se o conjunto nao for vazio insere fiz isso pq um for com 0 de tamanho nao executa pra atualizar
    #PRofessor
    # if resultProfessor.__len__()==0:
    #     for profnovo in professor:
    #         sql = ("INSERT INTO desenvolvimento_professor(nome, departamento_id, funcao, lattes, nomeEmCitacoesBibliograficas) VALUES ('%s' , %d , '%s', '%s', '%s')"                   % (profnovo.nome, profnovo.departamento, profnovo.funcao, profnovo.lattes, profnovo.nomeEmCitacoesBibliograficas))
    #         conector.execute(sql)
    #         connection.commit()
    # else:
    #     for p in professor:
    #         for row in resultProfessor:
    #             print(p.nome)
    #             if row[0] == p.nome and row[5] == p.lattes:
    #                 if row[3] != p.departamento or row[4] != p.funcao or row[5] != p.lattes or row[10] != p.nomeEmCitacoesBibliograficas:
    #                     sql = (
    #                     "UPDATE desenvolvimento_professor SET nome='%s', departamento_id=%d, funcao=%s, lattes=%s, nomeEmCitacoesBibliograficas=%s, enderecoProfissional=%s, endereco_profissional_lat=%s, endereco_profissional_long=%s Where nome=%s ",
    #                     (p.nome, p.departamento, p.funcao, p.lattes, p.nomeEmCitacoesBibliograficas, p.enderecoProfissional,
    #                      p.enderecoProfissional_lat, p.enderecoProfissional_long, p.nome))
    #                     conector.execute(sql)
    #                     connection.commit()
    #                     auxil = 1
    #         if auxil == 1:
    #             arraysProfNovo.append(p)
    #             auxil = 0
    #     for profnovo in arraysProfNovo:
    #         sql = ("INSERT INTO desenvolvimento_professor(nome, departamento_id, funcao, lattes, nomeEmCitacoesBibliograficas) VALUES ('%s' , %d , '%s', '%s', '%s')"
    #                % (profnovo.nome, profnovo.departamento, profnovo.funcao, profnovo.lattes, profnovo.nomeEmCitacoesBibliograficas))
    #         conector.execute(sql)
    #         connection.commit()
    #         auxiliar =0

    #projeto
    # if resultProfessor.__len__()==0:
    #     for profnovo in professor:
    #         sql = ("INSERT INTO desenvolvimento_professor(nome, departamento_id, funcao, lattes, nomeEmCitacoesBibliograficas) VALUES ('%s' , %d , '%s', '%s', '%s')"                   % (profnovo.nome, profnovo.departamento, profnovo.funcao, profnovo.lattes, profnovo.nomeEmCitacoesBibliograficas))
    #         conector.execute(sql)
    #         connection.commit()
    # else:
    for p in projetoPesquisa:
            # for row in resultProjeto:

        try:
            p1, p2 = (p.resumo.split("Descrição"))
            print(p1, "------------------------------------")
            # print()
        except UnicodeDecodeError:
            print("Erro")




        # print("descricao")
        #         situacao =
        #         natureza =
        #         integrantes =
        #         alunosEnvolvidos
        #
        #
        #     Descricao, Situacao, Natureza, Integrantes, AlunosEnvolvidos, Financiadores;
        #         # if row[0] == p.nome and row[5] == p.lattes:
    #                 if row[3] != p.departamento or row[4] != p.funcao or row[5] != p.lattes or row[10] != p.nomeEmCitacoesBibliograficas:
    #                     sql = (
    #                     "UPDATE desenvolvimento_professor SET nome='%s', departamento_id=%d, funcao=%s, lattes=%s, nomeEmCitacoesBibliograficas=%s, enderecoProfissional=%s, endereco_profissional_lat=%s, endereco_profissional_long=%s Where nome=%s ",
    #                     (p.nome, p.departamento, p.funcao, p.lattes, p.nomeEmCitacoesBibliograficas, p.enderecoProfissional,
    #                      p.enderecoProfissional_lat, p.   enderecoProfissional_long, p.nome))
    #                     conector.execute(sql)
    #                     connection.commit()
    #                     auxil = 1
    #         if auxil == 1:
    #             arraysProfNovo.append(p)
    #             auxil = 0
    #     for profnovo in arraysProfNovo:
    #         sql = ("INSERT INTO desenvolvimento_professor(nome, departamento_id, funcao, lattes, nomeEmCitacoesBibliograficas) VALUES ('%s' , %d , '%s', '%s', '%s')"
    #                % (profnovo.nome, profnovo.departamento, profnovo.funcao, profnovo.lattes, profnovo.nomeEmCitacoesBibliograficas))
    #         conector.execute(sql)
    #         connection.commit()
    #         auxiliar =0
    #
    #
    # # Artigo
    # if resultProfessor.__len__()==0:
    #     for profnovo in professor:
    #         sql = ("INSERT INTO desenvolvimento_professor(nome, departamento_id, funcao, lattes, nomeEmCitacoesBibliograficas) VALUES ('%s' , %d , '%s', '%s', '%s')"                   % (profnovo.nome, profnovo.departamento, profnovo.funcao, profnovo.lattes, profnovo.nomeEmCitacoesBibliograficas))
    #         conector.execute(sql)
    #         connection.commit()
    # else:
    #     for p in professor:
    #         for row in resultProfessor:
    #             print(p.nome)
    #             if row[0] == p.nome and row[5] == p.lattes:
    #                 if row[3] != p.departamento or row[4] != p.funcao or row[5] != p.lattes or row[10] != p.nomeEmCitacoesBibliograficas:
    #                     sql = (
    #                     "UPDATE desenvolvimento_professor SET nome='%s', departamento_id=%d, funcao=%s, lattes=%s, nomeEmCitacoesBibliograficas=%s, enderecoProfissional=%s, endereco_profissional_lat=%s, endereco_profissional_long=%s Where nome=%s ",
    #                     (p.nome, p.departamento, p.funcao, p.lattes, p.nomeEmCitacoesBibliograficas, p.enderecoProfissional,
    #                      p.enderecoProfissional_lat, p.enderecoProfissional_long, p.nome))
    #                     conector.execute(sql)
    #                     connection.commit()
    #                     auxil = 1
    #         if auxil == 1:
    #             arraysProfNovo.append(p)
    #             auxil = 0
    #     for profnovo in arraysProfNovo:
    #         sql = ("INSERT INTO desenvolvimento_professor(nome, departamento_id, funcao, lattes, nomeEmCitacoesBibliograficas) VALUES ('%s' , %d , '%s', '%s', '%s')"
    #                % (profnovo.nome, profnovo.departamento, profnovo.funcao, profnovo.lattes, profnovo.nomeEmCitacoesBibliograficas))
    #         conector.execute(sql)
    #         connection.commit()
    #         auxiliar =0
    #
    #
    #         #ArtigoEmConferencia
    # if resultProfessor.__len__()==0:
    #     for profnovo in professor:
    #         sql = ("INSERT INTO desenvolvimento_professor(nome, departamento_id, funcao, lattes, nomeEmCitacoesBibliograficas) VALUES ('%s' , %d , '%s', '%s', '%s')"                   % (profnovo.nome, profnovo.departamento, profnovo.funcao, profnovo.lattes, profnovo.nomeEmCitacoesBibliograficas))
    #         conector.execute(sql)
    #         connection.commit()
    # else:
    #     for p in professor:
    #         for row in resultProfessor:
    #             print(p.nome)
    #             if row[0] == p.nome and row[5] == p.lattes:
    #                 if row[3] != p.departamento or row[4] != p.funcao or row[5] != p.lattes or row[10] != p.nomeEmCitacoesBibliograficas:
    #                     sql = (
    #                     "UPDATE desenvolvimento_professor SET nome='%s', departamento_id=%d, funcao=%s, lattes=%s, nomeEmCitacoesBibliograficas=%s, enderecoProfissional=%s, endereco_profissional_lat=%s, endereco_profissional_long=%s Where nome=%s ",
    #                     (p.nome, p.departamento, p.funcao, p.lattes, p.nomeEmCitacoesBibliograficas, p.enderecoProfissional,
    #                      p.enderecoProfissional_lat, p.enderecoProfissional_long, p.nome))
    #                     conector.execute(sql)
    #                     connection.commit()
    #                     auxil = 1
    #         if auxil == 1:
    #             arraysProfNovo.append(p)
    #             auxil = 0
    #     for profnovo in arraysProfNovo:
    #         sql = ("INSERT INTO desenvolvimento_professor(nome, departamento_id, funcao, lattes, nomeEmCitacoesBibliograficas) VALUES ('%s' , %d , '%s', '%s', '%s')"
    #                % (profnovo.nome, profnovo.departamento, profnovo.funcao, profnovo.lattes, profnovo.nomeEmCitacoesBibliograficas))
    #         conector.execute(sql)
    #         connection.commit()
    #         auxiliar =0
    #
    # # ArtigoEmPeriodico
    # if resultProfessor.__len__()==0:
    #     for profnovo in professor:
    #         sql = ("INSERT INTO desenvolvimento_professor(nome, departamento_id, funcao, lattes, nomeEmCitacoesBibliograficas) VALUES ('%s' , %d , '%s', '%s', '%s')"                   % (profnovo.nome, profnovo.departamento, profnovo.funcao, profnovo.lattes, profnovo.nomeEmCitacoesBibliograficas))
    #         conector.execute(sql)
    #         connection.commit()
    # else:
    #     for p in professor:
    #         for row in resultProfessor:
    #             print(p.nome)
    #             if row[0] == p.nome and row[5] == p.lattes:
    #                 if row[3] != p.departamento or row[4] != p.funcao or row[5] != p.lattes or row[10] != p.nomeEmCitacoesBibliograficas:
    #                     sql = (
    #                     "UPDATE desenvolvimento_professor SET nome='%s', departamento_id=%d, funcao=%s, lattes=%s, nomeEmCitacoesBibliograficas=%s, enderecoProfissional=%s, endereco_profissional_lat=%s, endereco_profissional_long=%s Where nome=%s ",
    #                     (p.nome, p.departamento, p.funcao, p.lattes, p.nomeEmCitacoesBibliograficas, p.enderecoProfissional,
    #                      p.enderecoProfissional_lat, p.enderecoProfissional_long, p.nome))
    #                     conector.execute(sql)
    #                     connection.commit()
    #                     auxil = 1
    #         if auxil == 1:
    #             arraysProfNovo.append(p)
    #             auxil = 0
    #     for profnovo in arraysProfNovo:
    #         sql = ("INSERT INTO desenvolvimento_professor(nome, departamento_id, funcao, lattes, nomeEmCitacoesBibliograficas) VALUES ('%s' , %d , '%s', '%s', '%s')"
    #                % (profnovo.nome, profnovo.departamento, profnovo.funcao, profnovo.lattes, profnovo.nomeEmCitacoesBibliograficas))
    #         conector.execute(sql)
    #         connection.commit()
    #         auxiliar =0



    conector.close()
    connection.close()


if __name__ == "__main__":
    # executeLattes()
    executeLeitorXML()

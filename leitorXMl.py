from __future__ import print_function
from xml.dom import minidom
# from MySQLimport *
#
import mysql.connector


if __name__ == "__main__":
    x = minidom.parse('lattes/data/lattes-site/database.xml')
    CurriculoLattes = x.documentElement
    pesquisador = [Prof for Prof in CurriculoLattes.childNodes if Prof.nodeType == x.ELEMENT_NODE]

    # AbrindoConexao
    con = mysql.connector.connect(user='root', passwd='root', database='UTFPR')
    c = con.cursor()

    for prof in pesquisador:
        id = prof.getAttribute('id')
        nome_inicial = prof.getElementsByTagName("nome_inicial")[0]
        sexo = prof.getElementsByTagName("sexo")[0]
        nomeemCItacoes = prof.getElementsByTagName("nome_citacao_bibliografica")[0]



        # sql = "INSERT INTO desenvolvimento_funcionario(nome, email, telefone, departamento_id, funcao) " \
        #       "VALUES ( '%s', '%s', '%s', '%d', '%s' )" % (nome_inicial.firstChild.data, ' ', ' ', 1, 'Professor')
        # c.execute(sql)
        # con.commit()




        # sql="INSERT INTO desenvolvimento_funcionario(nome, email, telefone, departamento_id, funcao) " \
        # "VALUES ( '%s', '%s', '%s', '%d', '%s' )"  %(nome_inicial.firstChild.data, ' ', ' ', 1, 'Professor')
        # c.execute(sql);
        # # c.commit();
        # con.commit();
        # c.close();
        # con.close()


        # c.execute(
        sql= "INSERT INTO desenvolvimento_professor (nome, departamento_id, funcao, lattes,  nomeEmCitacoesBibliograficas) VALUES ('%s' , %d , '%s', '%s', '%s')" % ( nome_inicial.firstChild.data, 1, 'Professor', id, nomeemCItacoes.firstChild.data)
        c.execute(sql)

 # nome = models.CharField('Nome', max_length=100)
 #    email = models.CharField('E-mail', max_length=200)
 #    telefone = models.CharField('Telefone', max_length=20)
 #    departamento = models.ForeignKey(DepartamentoAcademico)
 #    funcao = models.CharField('Funcao', max_length=100)
 #    lattes = models.CharField('Link do Lattes', max_length=50)
 #    bolsaProdutividade = models.CharField('Bolsa Produtividade', max_length=100)
 #    enderecoProfissional = models.CharField('Endereco Profissional', max_length=5000)
 #    nomeEmCitacoesBibliograficas = models.CharField('nomeEmCitacoesBibliograficas', max_length=255)
 #    textoRe
        # print(sql)
        con.commit()

# c.close()
# con.close()
        projeto = prof.getElementsByTagName("projeto")
        for proj in projeto:
            try:
                ano_inicio = proj.getElementsByTagName('ano_inicio')[0]
                print('--> %s' % ano_inicio.firstChild.data)
            except IndexError:
                ano_inicio = ""
            try:
                ano_conclusao = proj.getElementsByTagName('ano_conclusao')[0]
            except IndexError:
                ano_conclusao = ""
            try:
                nome = proj.getElementsByTagName('nome')[0]
            except IndexError:
                nome = ""
            try:
                desc = proj.getElementsByTagName('descricao')[0]
            except IndexError:
                desc = ""
        # print('--> %s' % ano_inicio.firstChild.data)

    # con = mysql.connector.connect(user='root', passwd='root', database='UTFPR')
    # c = con.cursor()
        # # sql = "INSERT INTO desenvolvimento_projeto (dataInicio, datadeFim, nome, resumo) VALUES ('%s' , '%s', '%s' , '%s')" % (
    # #     ano_inicio.firstChild.data, ano_conclusao.firstChild.data, nome.firstChild.data, desc.firstChild.data)
    # c.execute(
    # "INSERT INTO desenvolvimento_projeto (dataInicio, listadeCoordenadores,listaColaboradores, AgendaFinanciadora,"
    # " datadeFim, nome, resumo)"
    #     " VALUES ('%s' , '%s', '%s', '%s',  '%s', '%s' , '%s')"
    #     % ( ano_inicio.firstChild.data, '', '', '', ano_conclusao.firstChild.data, nome.firstChild.data,
    #         desc.firstChild.data))
    con.commit()
    c.close()
    con.close()  # artigos = prof.getElementsByTagName("artigos_em_periodicos")  # for art in artigos:  # # try:
# doi = art.getElementsByTagName('doi')[0]
# # except IndexError, TypeError:
# #     doi. = ""
# # try:
#     titulo = art.getElementsByTagName('titulo')[0]
#     # except IndexError,  TypeError:
#     #     titulo = ""
#     # try:
#     autores = art.getElementsByTagName('autores')[0]
#     # except IndexError,  TypeError:
#     #     nome = ""
#     # try:
#     revista = art.getElementsByTagName('revista')[0]
#     # except IndexError,  TypeError:
#     #     revista = ""
#     # try:
#     volume = art.getElementsByTagName('volume')[0]
#     # except IndexError,  TypeError:
#     #     volume = ""
#     # try:
#     paginas = art.getElementsByTagName('paginas')[0]
#     # except IndexError,  TypeError:
#     #     paginas = ""
#     # try:
#     numero = art.getElementsByTagName('numero')[0]
#     # except IndexError,  TypeError:
#     #     numero = ""
#     # try:
#     ano = art.getElementsByTagName('ano')[0]
#     # except IndexError,  TypeError:
#     #     ano = ""
#
# # con = mysql.connector.connect(user='root', passwd='root', database='UTFPR')
# # c = con.cursor()
# # sql = "INSERT INTO desenvolvimento_artigo (titulo, listadeAutores, data, doi, paginas) VALUES ( '%s', '%s' ,'%s', '%s', '%s')" % \
# #       titulo.firstChild.data, autores.firstChild.data, ano.firstChild.data, doi.firstChild.data, paginas.firstChild.data
# #
# # sql2 = "SELECT id FROM desenvolvimento_artigo WHERE '%s " % titulo.firstChild.data
# #
# # sql3 = "INSERT INTO desenvolvimento_artigoemperiodico (artigo_ptr_id, nomeJournal, numero, volume) VALUES ('%s' , '%s', '%s' , '%s')" % (
# #     sql2, revista.firstChild.data, numero.firstChil.data, volume.firstChild.data)
# #
# # c.execute(sql)
# # con.commit()
# # c.execute(sql2)
# # con.commit()
# # c.execute(sql3)
# # con.commit()
# # c.close()
# # con.close()
#
#
#
# # paginaInicio = paginas.__getslice__()
# # con = mysql.connector.connect(user='root', passwd='root', database='UTFPR')
# # c = con.cursor()
# # sql = "INSERT INTO desenvolvimento_artigo (titulo, data, doi, paginaInicial, paginaFinal, Resumo) VALUES ('%s' , '%s', '%s' , '%s')" % (ano_inicio.firstChild.data, ano_conclusao.firstChild.data, nome.firstChild.data, desc.firstChild.data)
# # c.execute(sql)
# # con.commit()
# # c.close()
# # con.close()
#
# # con = mysql.connector.connect(user='root', passwd='root', database='UTFPR')
# # c = con.cursor()
# # sql = "INSERT INTO desenvolvimento_projeto (dataInicio, datadeFim, nome, resumo) VALUES ('%s' , '%s', '%s' , '%s')" % (ano_inicio.firstChild.data, ano_conclusao.firstChild.data, nome.firstChild.data, desc.firstChild.data)
# # c.execute(sql)
# # con.commit()
# # c.close()
# # con.close()
#
# # print ("%s" %titulo.childNodes[0].data)
# # print ("%s" %ano_inicio.childNodes[0].data)
# #
# # print ("%s" %ano_conclusao.childNodes[0].data)
# #
# # print ("%s" %nome.childNodes[0].data)
# #
# # print ("%s" %desc.childNodes[0].data)
#
#
#
# # projetos_pesquisa = [p for p in prof.childNodes if  p.nodeType == prof.ELEMENT_NODE]
# # for po in projetos_pesquisa:
# # projeto = [pr for pr in po.childNodes if pr.nodeType == po.ELEMENT_NODE]
# # print("%s" %po)
# #
# # for pa in projeto:
# #         #print("%s" %pa)
# #
# #         ano  = pa.getElementsByTagName("ano_inicio")[0]
# #         print("%s" %ano.firstChild.data)
# #              # projeto = prof.getElementsByTagName("projeto")[0]
# # #print("%s" % ano.firstChild.data)
# # # for pr in projeto:
# # #
# # #     ano = pr.projeto.getElementsByTagName("ano_inicio")[0]
# # #     #ano  = projeto.getElementsByTagName("ano_inicio")[0]
# #     for a in projeto:
# #         print("%s" % a.getElementsByTagName("ano_inicio")[0].getfirstChild.data)
# # except IndexError:
# #     ano_inicio = ""
# # ano_inicio:
#
#
# # projeto = prof.getElementsByTagName("projeto")[0]
# # for p in projeto :
# #     ano_inicio = p.getElementsByTagName("ano_inicio")[0]
# # #for p  in ano_inicio:
# #     print("%s" % ano_inicio.firstChild.data)
#
# # print'-----> %s' % sexo.firstChild.data
# # print '---->%s' % endereco_profissional.firstChild.data
# # print '-->'
#
#
#
#
# #  projeto=CurriculoLattes.documentElement
#
# #projetos_pesquisa = prof.getElementsByTagName("projetos_pesquisa")
# #print ("%s") %projetos_pesquisa.childNodes.data
# #
# # projeto  = [ p for p in CurriculoLattes.childNodes if p.nodeType == x.ELEMENT_NODE]
# # #projeto = [projs for projs in prof.childNodes if projs.nodeType == CurriculoLattes.ELEMENT_NODE]
# #
# # for projet in projeto:
# #     #projetos_pesquisa = CurriculoLattes.documentElement
# #     projetos_pesquisa = projet.getElementsByTagName("projetos_pesquisa")
# #
# #     #projeto = projet.firstChild.childNodes
# #     # for p in projeto:
# #     #projs = projeto.getElementsByTagName('projetos_pesquisa')
# #     ano_inicio = projetos_pesquisa.getElementsByTagName("ano_inicio")[0]
# #     #.getAttribute("ano_inicio")
# #     #
# #     #try:
# #     #   ano_conclusao = projeto.getElementsBytagName("ano_conclusao")
# #     #catch():
# #     #ano_conclusao = ""
# #     # nomeDoProjeto = p.getElementsByTagName("nome")
# #     # descricao = p.getElementsByTagName("descricao")
# #
# #     #    print
# #     #print("%s") % p.firstChild.data
# #     print("%s" % ano_inicio.firstChild.data)
# #     # print(  "---> %s" % ano_conclusao.firstChild.data)
# #     # print ('-----> %s' % nomeDoProjeto)
# #     # print ('---->%s' % descricao)
# #     #     # nome_completo = ident.getElementsBytagName('nome_completo')
# #     # staff.getElementsByTagName("salary")[0]
# #     # print "----> %s" % ident


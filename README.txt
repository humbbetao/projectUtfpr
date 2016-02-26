Projeto de desenvolvimento de site para o Departamento de Computação - UTFPR-CM


Como instalar:

===============
Desenvolvimento
==============


Pacote de Desenvolvimento-app. Web-site desenvolvimento em django, com base em python.
Utilizado para apresentar os artigos, projetos e eventos do Departamento de Computação- UTFPR-CM


Quick start
--------------------------------------------------------------------------

1. Baixar Django,Haystack,Whoosh,Banco de dados de preferência MySQL;

2. Baixar o projeto do repositório: https://github.com/humbbetao/projectutfpr.

3. Criar no banco de dados uma nova instância banco, de preferência nomeio com 'UTFPR'.

4. Dentro da pasta projectUtfpr tem settings.py, procure dentro desse arquivo:

"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'UTFPR',  # nome da instancia de banco de dados
        # The following settings are not used with sqlite3:
        'USER': 'root',  # usuário do banco de dados
        'PASSWORD': 'Humberto1!',  #senha
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}
"
	Modifique 'NAME', 'USER', 'PASSWORD', 'HOST', 'PORT' para as suas configurações;
  
5.
	1. Executar os seguintes comando como root, python manage.py migrate, esse comando criará as tabelas no banco de dados;
	2.Executar os seguintes comando como root, python manage.py syncdb, esse comando realizará a configuração do admin do projeto Django, defina seu login e senha do Django;

	3. Executar os seguintes comando como root, python manage.py runserver, se tudo estiver  ok aparecerá o link do site aparecerá, assim visite http://127.0.0.1:8000/admin/ utilize seu login e senha do Django para entrar na adm da página, e http://127.0.0.1:8000/desenvolvimento/ para entrar no site;


6.  À partir daqui você deve ver o site, sem contéudo.
    Algo como  página 1 de 1 deverá ser visualizado em algumas páginas;
    Para preencher os dados, execute um desses comandos;

    
	1. entre na pasta desenvolvimento/lattes/scriptlattes/data/
        no arquivo lattes-dacom.csv insira os dados dos membros
        na seguinte ordem: numero do lattes, nome do membro, e função;

        ou

        2. siga as instruções de como baixar manualmente os dados do lattes, no site http://scriptlattes.sourceforge.net/

7. entre na pasta, desenvolvimento/lattes/scriptlattes/
        execute o comando 'python leitoXMLnovo.py'   esse comando percorrer os dados e populara o banco de dados


8. Visite http://127.0.0.1:8000/desenvolvimento/ para ver se tudo esta ok;


9. Para habilitar a pesquisa execute o comando 'python manage.py update_index'


Dependências:
    ScriptLattes >= 8.10
    Django >= 1.7
    Django-Celery>= 3.0
    Haystack >=2.0.0
    Whoosh >=2.0
    djangocms-installer>=-0.8.7







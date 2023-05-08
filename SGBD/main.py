#Arquivo de testes de desenvolvimento
from Libs.SGBD import SGBD

MySGBD = SGBD().set_database_archive('Data/example.txt')

# seta o um registro atravez de um dicionarios com os atributos correspondentes
MySGBD.set_register({'Titulo': 'Final Fantasy Y',    'Produtora': 'Square Enix',
                     'Genero': 'Action RPG',          'Plataforma': 'Multplataforma',
                     'Ano': '2014',                   'Classificacao': 'Teen',
                     'Preco': '125.0',                'Midia': 'Ambos',
                     'Tamanho': '100.5'}).write()

MySGBD.set_register({'Titulo': 'Final Fantasy X',    'Produtora': 'Square Enix',
                     'Genero': 'Action RPG',          'Plataforma': 'Multplataforma',
                     'Ano': '2014',                   'Classificacao': 'Teen',
                     'Preco': '125.0',                'Midia': 'Ambos',
                     'Tamanho': '100.5'}).write()

MySGBD.show()
from Libs.SGBD import SGBD

MySGBD = SGBD().set_database_archive("Data/example.txt")

#O metodo set_attribute pode ser encadeado com diversos outros métodos
MySGBD.set_attribute('Titulo',"The Wither 2")
MySGBD.set_attribute('Produtora',"Riot Games")
MySGBD.set_attribute('Genero',"RPG")
MySGBD.set_attribute('Plataforma',"Xbox")
MySGBD.set_attribute('Ano',"2010")
MySGBD.set_attribute('Classificacao',"16+")
MySGBD.set_attribute('Preco',"99.0")
MySGBD.set_attribute('Midia',"Digital")
MySGBD.set_attribute('Tamanho',"15.5")
MySGBD.write()


# seta o um registro atravez de um dicionarios com os atributos correspondentes
registro = {'Titulo': 'Final Fantasy XV',    'Produtora': 'Square Enix',
            'Genero': 'Action RPG',          'Plataforma': 'Multplataforma',
            'Ano': '2014',                   'Classificacao': 'Teen',
            'Preco': '125.0',                'Midia': 'Ambos',
            'Tamanho': '100.5'}
MySGBD.set_register(registro).write()


# seta o registro com chamada mista de metodos
registro = {'Titulo': 'Hollow Knight',       'Produtora': 'Square Enix',
            'Genero': 'Metroidvania',        'Plataforma': 'Multplataforma',
            'Ano': '2011',                   'Classificacao': 'Teen',
            'Tamanho': "20",                 'Midia': 'Ambos',
            }
MySGBD.set_register(registro).set_attribute('Preco', '125.0').write()

# Exibe a database bem indentada
MySGBD.show()

#Pesquisa linear no banco
print(MySGBD.grep('Fantasy'))
print(MySGBD.grep_register('Fantasy'))

#deleta o quinto registro da base, e atualiza o top
MySGBD.delete(2)

#Exibe o cabeçalho do arquivo de banco de dados
print("\n")
print(MySGBD.Header())

# #deleta todo registro que tem Multplataforma em algum lugar 
# #método ainda não recomendado, possui alguns bugs as referencias de arquivos deletados
# [MySGBD.delete(i) for i in MySGBD.grep("Multplataforma")]

# #deleta o registro com a chave primaria FinalFantasyX2014
# MySGBD.delete(MySGBD.grep_by_fk("FinalFantasyX2014"))

# #execute este arquivo para ver ao vivaço as alterações em example.txt
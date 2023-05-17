from Libs.SGBD import SGBD

MySGBD = SGBD().set_database_archive("Data/example.txt")

# seta os atributos por encadeamento de metodos
(MySGBD.set_attribute('Titulo',"The Wither 2")
.set_attribute('Produtora',"Riot Games")
.set_attribute('Genero',"RPG")
.set_attribute('Plataforma',"Multplataforma")
.set_attribute('Ano',"2010")
.set_attribute('Classificacao',"16+")
.set_attribute('Preco',"99.0")
.set_attribute('Midia',"Digital")
.set_attribute('Tamanho',"15.5")
.write())


# seta o um registro atravez de um dicionarios com os atributos correspondentes
MySGBD.set_register({'Titulo': 'Final Fantasy XV',    'Produtora': 'Square Enix',
                     'Genero': 'Action RPG',          'Plataforma': 'Multplataforma',
                     'Ano': '2014',                   'Classificacao': 'Teen',
                     'Preco': '125.0',                'Midia': 'Ambos',
                     'Tamanho': '100.5'}).write()


# seta o registro com chamada mista de metodos
MySGBD.set_register({'Titulo': 'Hollow Knight',       'Produtora': 'Square Enix',
                     'Genero': 'Metroidvania',        'Plataforma': 'Multplataforma',
                     'Ano': '2011',                   'Classificacao': 'Teen',
                    }).set_attribute('Tamanho',"20").set_attribute('Midia', 'Ambos').set_attribute('Preco', '125.0').write()

# Exibe a database bem indentada
MySGBD.show()

#Pesquisa linear no banco ("""""linear""""", entre muitas aspas. Por enquando le o bando todo e procura na memoria)
print(MySGBD.grep('Fantasy'))
print(MySGBD.grep_register('Fantasy')) # Pode printar na tela este registro, caso queira entender a estrutura

#Exibe o cabeçalho do arquivo de banco de dados
print("\n")
print(MySGBD.Header())

#deleta o quinto registro da base, e atualiza o top
MySGBD.delete(5)

#deleta todo registro que tem Multplataforma em algum lugar 
[MySGBD.delete(i) for i in MySGBD.grep("Multplataforma")]

#deleta o registro com a chave primaria FinalFantasyX2014
MySGBD.delete(MySGBD.grep_by_fk("FinalFantasyX2014"))

#execute este arquivo para ver ao vivaço as alterações em example.txt
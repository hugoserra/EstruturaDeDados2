from Libs.SGBD import SGBD
import pandas as pd #Pandas apenas é utilizado para fins de exibição indentada no terminal, nada mais.
pd.set_option('display.max_rows', None)

MySGBD = SGBD('delimiter')#Escolhe qual estrategia de gravação e recuperação vai utilizar, utiliza por padrão DB_delimiter.txt como base de dados

# MySGBD.database.set_database_archive("Data/example.txt")#Define um arquivo de banco de dados de exemplo

#seta os atributos
# MySGBD.set_attribute('Titulo',"The Wither 2")
# MySGBD.set_attribute('Produtora',"Riot Games")
# MySGBD.set_attribute('Genero',"RPG")
# MySGBD.set_attribute('Plataforma',"Multplataforma")
# MySGBD.set_attribute('Ano',"213")
# MySGBD.set_attribute('Classificacao',"16+")
# MySGBD.set_attribute('Preco',"99.0")
# MySGBD.set_attribute('Midia',"Digital")
# MySGBD.set_attribute('Tamanho',"15.5")
# MySGBD.write()

#Exibe os dados
# print(pd.DataFrame(MySGBD.read()))

#Pesquisa linear no banco
print(MySGBD.database.grep('Horizon Zero Dawn'))
print(MySGBD.database.grep_register('Horizon Zero Dawn'))

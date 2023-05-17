#Arquivo de testes de desenvolvimento
from Libs.SGBD import SGBD

MySGBD = SGBD().set_database_archive('Data/example.txt')

MySGBD.delete(MySGBD.grep("FinalFantasyX2014"))

#deleta todo registro que tem Multplataforma em algum lugar 
[MySGBD.delete(i) for i in MySGBD.grep("Multplataforma")]
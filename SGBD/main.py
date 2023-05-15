#Arquivo de testes de desenvolvimento
from Libs.SGBD import SGBD

MySGBD = SGBD().set_database_archive('Data/example.txt')


MySGBD.DB.storage_compact()
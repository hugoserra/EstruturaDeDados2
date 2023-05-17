#Arquivo de testes de desenvolvimento
from Libs.SGBD import SGBD

MySGBD = SGBD().set_database_archive('Data/AT02-CasosDeTeste/input1.txt')
MySGBD.show()
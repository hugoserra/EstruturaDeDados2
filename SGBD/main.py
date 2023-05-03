from Libs.SGBD import SGBD
import pandas as pd #Pandas apenas é utilizado para fins de exibição indentada no terminal, nada mais.
pd.set_option('display.max_rows', None)

Games = SGBD()
Games.set_database_archive("Data/games.txt")

#Casa base utiliza uma estrategia
MySGBD = SGBD()

for register in Games.read():
    MySGBD.set_register(register).write()

MySGBD.show()

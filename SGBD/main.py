from Libs.SGBD import SGBD

Games = SGBD().set_database_archive("Data/games.txt")
MySGBD = SGBD() #utiliza DB_delimiter.txt como base padrao

for register in Games.read():
    MySGBD.set_register(register).write()

MySGBD.show()

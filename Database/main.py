from Libs.Database import Database, Register

DB = Database().validate()
DB.set_database_archive("Metadados/DB.txt")

register = Register()
register.set_attribute('nome','The Wither 2', 50)
register.set_attribute('Preco','150', 5)
register.set_attribute('Categoria','Medieval', 15)
register.set_attribute('Idade','15', 3)
DB.set_fixed_register(register)

register.set_attribute('nome','Assassins Creed', 50)
register.set_attribute('Preco','139', 5)
register.set_attribute('Categoria','Medieval', 15)
register.set_attribute('Idade','19', 3)
DB.set_fixed_register(register)

registers = DB.get_fixed_registers()
print(registers)





























#a

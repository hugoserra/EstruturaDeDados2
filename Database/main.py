from Libs.Database import Database, Register

DB = Database().validate()
DB.set_database_archive("Metadados/DB.txt")

DB.register.set_attribute('nome','The Wither 2', 50)
DB.register.set_attribute('Preco','150', 5)
DB.register.set_attribute('Categoria','Medieval', 15)
DB.register.set_attribute('Idade','15', 3)
DB.set_fixed_register()

DB.register.set_attribute('nome','Assassins Creed',50)
DB.register.set_attribute('Preco','139',5)
DB.register.set_attribute('Categoria','Medieval',15)
DB.register.set_attribute('Idade','19',3)
DB.set_fixed_register()

registers = DB.get_fixed_registers({"nome":49, "Preco":4, "Categoria":14, "Idade":2})
print(registers)





























#a

from Libs.Files import DatabaseFile

class Tools:

    def set_size(self,str,size):
        return f"{str}" + (size-len(str)) * " "


class Register:

    def set_attribute(self,name,value):
        self.__dict__[name] = value

    def get_attributes(self):
        return self.__dict__.copy()


class Database(Tools):

    def __init__(self):
        self.database = DatabaseFile("Metadados/games.txt")
        self.register = Register()

    def set_database_archive(self,archive_name):
        self.database = DatabaseFile(archive_name)


class DatabaseFixed(Database):

    def __init__(self):
        super().__init__()
        self.register_size = {"Titulo":50, "Produtora":40, "Genero":25, "Plataforma":15, "Ano":4, "Classificacao":12, "Preco":7, "Midia":8, "Tamanho":7}

    def write(self):
        register_fixed_size = ""

        for key, value in self.register_size.items():
            attribute = self.register.get_attributes()[key] if(key in self.register.get_attributes()) else ""
            register_fixed_size += self.set_size(attribute,self.register_size[key])

        self.database.write(f"{register_fixed_size}\n")
        self.register = Register()

    def read(self):
        self.database.pointer_reset()
        registers = []

        for str_register in self.database.archive.readlines():
            register = Register()
            pointer = 0
            for attribute, size in self.register_size.items():
                register.set_attribute(attribute, str(str_register[pointer:pointer+size]).strip())
                pointer += size
            registers.append(register.get_attributes())

        return registers




















        #

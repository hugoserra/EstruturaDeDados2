from Libs.Files import DatabaseFile

class Register:

    def set_attribute(self,name,value):
        self.__dict__[name] = value

    def set_register(self,dict):
        self.__dict__ = dict.copy()

    def get_attributes(self):
        return self.__dict__.copy()


class DatabaseTools:

    def set_pipe(self,str):
        return f"{str}|"

    def grep(self,consulta):

        linhas = self.DB_File.readlines()
        indexs = []

        for i, linha in enumerate(linhas):
            if linha.find(consulta) != -1:
                indexs.append(i)

        return indexs

    def grep_register(self,consulta):
        return [self.read()[x] for x in self.grep(consulta)];

    def set_database_archive(self,archive_name):
        self.DB_File = DatabaseFile(archive_name)


class Database(DatabaseTools):

    def __init__(self):
        self.DB_File = DatabaseFile("Data/games.txt")
        self.register = Register()
        self.fields = ["Titulo", "Produtora", "Genero", "Plataforma", "Ano", "Classificacao", "Preco", "Midia", "Tamanho"]

    def write(self):
        register_fixed_fields = ""

        for key in self.fields:
            attribute = self.register.get_attributes()[key] if(key in self.register.get_attributes()) else ""
            register_fixed_fields += self.set_pipe(attribute)

        self.DB_File.write(f"{register_fixed_fields}\n")
        self.register = Register()

    def read(self):
        registers = []

        for str_register in self.DB_File.readlines():
            register = Register()
            str_register = str_register[:-1]
            attributes = str_register.split("|")
            register.set_register(dict(zip(self.fields, attributes)))
            registers.append(register.get_attributes())

        return registers

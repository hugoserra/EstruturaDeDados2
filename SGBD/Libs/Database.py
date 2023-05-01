from Libs.Files import DatabaseFile

class Tools:

    def set_size(self,str,size):
        return f"{str}" + (size-len(str)) * " "

    def set_pipe(self,str):
        return f"{str}|"

    def split_by_size(self,str,size):
        pointer = 0
        registers = []
        for register_size in range(size,len(str)+1,size):
            registers.append(str[pointer:register_size])
            pointer = register_size

        return registers

    def split_by_bytes(self,str):

        bytes, size, registers, pointer = int(str.split('|')[0]), len(str), [], 0
        while(pointer < size):
            attributes = str[pointer:pointer+bytes].split("|")
            attributes.pop(0)
            if(bytes != 1):
                registers.append(attributes)
            pointer += bytes
            bytes = str[pointer: pointer+str[pointer:].find('|')]
            bytes = int(bytes) if(bytes != "") else 1


        return registers

    def grep(self,consulta):

        self.database.pointer_reset()
        linhas = self.database.archive.readlines()
        indexs = []

        for i, linha in enumerate(linhas):
            campos = linha.strip().split('|')
            if consulta in campos:
                indexs.append(i)

        return indexs

    def grep_register(self,consulta):
        return [self.read()[x] for x in self.grep(consulta)];


class Register:

    def set_attribute(self,name,value):
        self.__dict__[name] = value

    def set_attributes(self,dict):
        self.__dict__ = dict.copy()

    def get_attributes(self):
        return self.__dict__.copy()


class Database(Tools):

    def __init__(self):
        self.database = DatabaseFile("Data/games.txt")
        self.register = Register()

    def set_database_archive(self,archive_name):
        self.database = DatabaseFile(archive_name)


class DatabaseFixedSize(Database):

    def __init__(self):
        super().__init__()
        self.register_size = {"Titulo":50, "Produtora":40, "Genero":25, "Plataforma":15, "Ano":4, "Classificacao":12, "Preco":7, "Midia":8, "Tamanho":7}
        self.size = 50+40+25+15+4+12+7+8+7

    def write(self):
        register_fixed_size = ""

        for key, value in self.register_size.items():
            attribute = self.register.get_attributes()[key] if(key in self.register.get_attributes()) else ""
            register_fixed_size += self.set_size(attribute,self.register_size[key])

        self.database.write(f"{register_fixed_size}")
        self.register = Register()

    def read(self):
        self.database.pointer_reset()
        registers = []

        for str_register in self.split_by_size(self.database.archive.read(),self.size):
            register = Register()
            pointer = 0
            for attribute, size in self.register_size.items():
                register.set_attribute(attribute, str(str_register[pointer:pointer+size]).strip())
                pointer += size
            registers.append(register.get_attributes())

        return registers


class DatabaseFixedFields(Database):

        def __init__(self):
            super().__init__()
            self.fields = ["Titulo", "Produtora", "Genero", "Plataforma", "Ano", "Classificacao", "Preco", "Midia", "Tamanho"]

        def write(self):
            register_fixed_fields = ""

            for key in self.fields:
                attribute = self.register.get_attributes()[key] if(key in self.register.get_attributes()) else ""
                register_fixed_fields += self.set_pipe(attribute)

            self.database.write(f"{register_fixed_fields}")
            self.register = Register()

        def read(self):
            self.database.pointer_reset()
            registers = []

            register, count, attributes = Register(), 0, []
            for attribute in self.database.archive.read().split("|"):

                if(count == len(self.fields)):
                    register.set_attributes(dict(zip(self.fields, attributes)))
                    registers.append(register.get_attributes())
                    register, count, attributes = Register(), 0, []


                if(count < len(self.fields)):
                    attributes.append(attribute)
                    count+=1



            return registers


class DatabaseSizeBytes(Database):

        def __init__(self):
            super().__init__()
            self.fields = ["Titulo", "Produtora", "Genero", "Plataforma", "Ano", "Classificacao", "Preco", "Midia", "Tamanho"]

        def write(self):
            register_fixed_fields = ""

            for key in self.fields:
                attribute = self.register.get_attributes()[key] if(key in self.register.get_attributes()) else ""
                register_fixed_fields += self.set_pipe(attribute)

            self.database.write(f"{len(register_fixed_fields)+len(str(len(register_fixed_fields)))+1}|{register_fixed_fields}")
            self.register = Register()

        def read(self):
            self.database.pointer_reset()
            registers = []

            for attributes in self.split_by_bytes(self.database.archive.read()):
                register = Register()
                register.set_attributes(dict(zip(self.fields, attributes)))
                registers.append(register.get_attributes())

            return registers


class DatabaseDelimiter(Database):

        def __init__(self):
            super().__init__()
            self.fields = ["Titulo", "Produtora", "Genero", "Plataforma", "Ano", "Classificacao", "Preco", "Midia", "Tamanho"]

        def write(self):
            register_fixed_fields = ""

            for key in self.fields:
                attribute = self.register.get_attributes()[key] if(key in self.register.get_attributes()) else ""
                register_fixed_fields += self.set_pipe(attribute)

            self.database.write(f"{register_fixed_fields}\n")
            self.register = Register()

        def read(self):
            self.database.pointer_reset()
            registers = []

            for str_register in self.database.archive.readlines():
                register = Register()
                str_register = str_register[:-1]
                attributes = str_register.split("|")
                register.set_attributes(dict(zip(self.fields, attributes)))
                registers.append(register.get_attributes())

            return registers

from Libs.Files import DatabaseFile

class Tools:

    def set_size(self,str,size):
        return f"{str}" + (size-len(str)-1) * " "

class Register(Tools):

    def __init__(self):
        self.size = {}

    def set_attribute(self,name,value,size=None):
        self.__dict__[name] = value if(size == None) else self.set_size(value,size)
        self.size[name] = len(value)

    def get_attributes(self):
        dict = self.__dict__.copy()
        dict.pop('size')
        return dict

class Database(Tools):

    def __init__(self):
        self.database = DatabaseFile("Metadados/games.txt")
        self.register = Register()
        self.register_size = {}

    def validate(self):
        if(self.database.validate()):
            return self

        return False

    def set_database_archive(self,archive_name):
        self.database = DatabaseFile(archive_name)
        self.database.validate()

    def set_fixed_register(self):

        register_fixed_size = ""
        for key, value in self.register.get_attributes().items():
            self.register_size[key] = len(value)
            register_fixed_size += value

        self.database.write(f"{register_fixed_size}\n")

    def get_fixed_registers(self,register_size=None):
        if(register_size != None):
            self.register_size = register_size

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

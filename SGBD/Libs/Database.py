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

    #Está é uma busca linear, diferente da implementação anterior.
    #Assim, o arquivo não é inteiro alocado na memória para executar a busca
    def grep(self,search):
        self.DB_File.pointer_reset()
        indexs, line, i = [], self.DB_File.readline(), 0
        while line != None:
            if(line.find(search) != -1):
                indexs.append(i)
            line, i = self.DB_File.readline(), i+1

        return indexs

    #Tem as mesmas propriedades do metodo acima, e como na função grep do linux,
    #retorna a linha do arquivo assim como esta escrita, e não o registro da linha correspondente
    def grep_register(self,search):
        self.DB_File.pointer_reset()
        lines, line = [], self.DB_File.readline()
        while line != None:
            if(line.find(search) != -1):
                lines.append(line)
            line = self.DB_File.readline()

        return lines

    #retorna os registros correspondentes em forma de dicionario, onde os atributos podem ser recuperados
    #mas não é uma função linear pois aloca toda a base na memoria ram (será atualizada futuramente)
    def get_registers(self,search):
        return [self.read()[x] for x in self.grep(search)]

    def set_database_archive(self,archive_name):
        self.DB_File = DatabaseFile(archive_name)
        return self.scrap_header(str(self.DB_File.get_first_line()))
    
    def scrap_header(self,header_str):
        header = {}
        attributes = header_str.split(',')
        for attribute in attributes:
            key_value = attribute.split('=')
            try:
                key_value[1] = int(key_value[1])
            except:
                pass
            header[key_value[0]] = key_value[1]
        return header




class Database(DatabaseTools):

    def __init__(self):
        self.Header = self.set_database_archive("Data/DB_delimiter.txt")
        print(self.Header)
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

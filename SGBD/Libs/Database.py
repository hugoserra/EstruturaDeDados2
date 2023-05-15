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

    def set_database_archive(self,archive_name):
        self.DB_File = DatabaseFile(archive_name)
        self.Header = self.get_header()

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
    
    def get_header(self):
        header_str = self.DB_File.get_header()
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
    
    def update_header(self):
        header_str = ''
        for key,value in self.Header.items(): 
            header_str += f"{key}={value},"
        
        header_str = f"{header_str[:-1]}"
        self.DB_File.set_header(header_str)
        
    

class Database(DatabaseTools):

    def __init__(self):
        self.set_database_archive("Data/DB_delimiter.txt")
        self.Header = self.get_header()
        self.fields = ["Titulo", "Produtora", "Genero", "Plataforma", "Ano", "Classificacao", "Preco", "Midia", "Tamanho"]
        self.register = Register()
        
    def write(self):
        register_fixed_fields = ""

        for key in self.fields:
            attribute = self.register.get_attributes()[key] if(key in self.register.get_attributes()) else ""
            register_fixed_fields += self.set_pipe(attribute)

        self.DB_File.write(f"{register_fixed_fields}\n")
        self.register = Register()

        self.Header['REG_N'] += 1
        self.update_header()

    def read(self):
        registers = []

        for str_register in self.DB_File.readlines():
            register = Register()
            str_register = str_register[:-1]
            attributes = str_register.split("|")
            register.set_register(dict(zip(self.fields, attributes)))
            registers.append(register.get_attributes())

        return registers
    
    def delete(self,index):

        self.DB_File.pointer_reset()

        for x in range(0,index-1):
            line = self.DB_File.archive.readline()
            if(line == ""):
                return 0
            
        self.DB_File.archive.seek(self.DB_File.archive.tell())#Aponta o ponteiro de leitura para o inicio do arquivo
        self.DB_File.archive.write(f"*{self.Header['TOP']}|")

        self.Header['TOP'] = index;
        self.update_header()


            


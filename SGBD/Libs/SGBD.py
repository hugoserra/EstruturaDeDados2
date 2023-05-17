from Libs.Database import Database
import pandas as pd #Pandas apenas é utilizado para fins de exibição indentada no terminal, nada mais.

# A class SGBD é uma fachada para a manipulaçao da database, pode ser utilizada para 
# auxiliar na compreensao do código.
class SGBD:

    def __init__(self):
        self.type = type
        self.DB = None
        self.config()

    def config(self):
        self.DB = Database() # a classe Database é responsavel por todas as operações de r+ na base.txt

    def set_attribute(self,name,value):
        self.DB.register.set_attribute(name,value)
        return self

    def set_register(self,register):
        self.DB.register.set_register(register)
        return self

    def write(self):
        self.DB.write()

    def read(self):
        return self.DB.read()

    def show(self):
        show = pd.DataFrame(self.DB.read())
        print(f"\n{show}\n")
        return show

    def grep(self,consulta):
        return self.DB.grep(consulta)

    def grep_register(self,consulta):
        return self.DB.grep_register(consulta)

    def set_database_archive(self,archive):
        self.DB.set_database_archive(archive)
        return self
    
    def Header(self):
        return self.DB.Header
    
    def delete(self,index):
        self.DB.delete(index)
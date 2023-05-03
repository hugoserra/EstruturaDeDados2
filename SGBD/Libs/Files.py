class DatabaseFile:#Esta classe recebera a base de dados

    def __init__(self,archive_name):
        self.archive_name = archive_name
        self.archive = open(self.archive_name,'a+')

    def write(self,register):
        self.archive.write(register)

    def read(self):
        return self.pointer_reset().read()

    def readline(self):
        line = self.archive.readline()
        return line if line != "" else None

    def readlines(self):
        return self.pointer_reset().readlines()

    def pointer_reset(self):
        self.archive.seek(0, 0)#Aponta o ponteiro de leitura para o inicio do arquivo
        return self.archive

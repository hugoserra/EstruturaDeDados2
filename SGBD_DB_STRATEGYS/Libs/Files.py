class DatabaseFile:#Esta classe recebera a base de dados

    def __init__(self,archive_name):
        self.archive_name = archive_name
        self.archive = open(self.archive_name,'a+')

    def write(self,register):
        self.archive.write(register)

    def read(self):
        self.pointer_reset()
        return self.archive.read()

    def pointer_reset(self):
        self.archive.seek(0, 0)#Aponta o ponteiro de leitura para o inicio do arquivo
        return self.archive

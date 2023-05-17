class DatabaseFile:#Esta classe recebera a base de dados

    def __init__(self,archive_name):
        self.archive_name = archive_name
        self.archive = open(self.archive_name,'r+')

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
        self.archive.readline()
        return self.archive
    
    def get_header(self):
        self.archive.seek(0, 0)#Aponta o ponteiro de leitura para o inicio do arquivo
        header = self.archive.readline()[:-1]

        if(len(header) <= 10): #se cabeçalho invalido
            header = f"REG_N=0,TOP=-1" #caso o cabeçalho seja invalido, usará este como padrao
            self.archive.seek(0, 0)#Aponta o ponteiro de leitura para o inicio do arquivo
            self.archive.write(f"{header}{50*' '}\n")

        return header
    
    def set_header(self,header):
        tell = self.archive.tell()#Captura a posição atual do ponteiro

        self.archive.seek(0, 0)#Aponta o ponteiro de leitura para o inicio do arquivo
        self.archive.write(f"{header}         ")

        self.archive.seek(tell)
class DatabaseFile:#Esta classe recebera a base de dados

    def __init__(self,archive_name):
        self.validation_status = "passed";
        self.archive = None
        self.archive_name = archive_name

    def validate(self):
        #este método faz a validação do arquivo de entrada, utilizando os métodos abaixo:

        self.check_if_exist()

        if(self.validation_status == "passed"):
            return True
        else:
            self.archive = None
            print(self.validation_status)#exibe o tipo do erro que os metodos check encontraram
            return False

        #se tudo correr bem, este metodo retorna true, indicando que o arquivo de entrada já esta atribuido
        #ao atributo self.archive

    def check_if_exist(self):
        if(self.validation_status != "passed"):
            return False

        try:
            archive = open(self.archive_name,'a+')
            self.archive = archive
        except Exception as e:
            self.validation_status = "The chosen file does not exist."

    def write(self,register):
        self.archive.write(register)

    def read(self):
        self.pointer_reset()
        return self.archive.read()

    def pointer_reset(self):
        self.archive.seek(0, 0)#Aponta o ponteiro de leitura para o inicio do arquivo
        return self.archive

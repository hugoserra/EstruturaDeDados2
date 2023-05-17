#Arquivo de testes de desenvolvimento
from Libs.SGBD import SGBD
import sys

class AT2_Facade:

    def __init__(self):
        self.validate()

    def validate(self):

        if(len(sys.argv) != 5):
            print("\n\nARGV Não recebeu todos os parametros necessários!\n\n")
            return
        
        try:
            self.set_input_archive()
            self.set_options_archive()
            self.make_temp_archive()
            self.make_output_archive()
        except Exception as E:
            print(f"\n\nOcorreu um erro na abertura ou leitura de um arquivo!\n\n{E}\n\n")

    def set_input_archive(self):
        self.MySGBD = SGBD().set_database_archive(f'{sys.argv[1]}')

    def set_options_archive(self):
        self.options_archive = open(f'{sys.argv[2]}',"r+")

    def make_temp_archive(self):
        self.temp_archive = open(f'{sys.argv[3]}',"a+")

    def make_output_archive(self):
        self.output_archive = open(f'{sys.argv[4]}',"a+")


run = AT2_Facade()
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
            self.make_temp_archive()
            self.set_and_exec_options_archive()
            self.make_output_archive()
        except Exception as E:
            print(f"\n\nOcorreu um erro na abertura ou leitura de um arquivo!\n\n{E}\n\n")

    def set_input_archive(self):
        self.MySGBD_input = SGBD().set_database_archive(f'{sys.argv[1]}')

    def set_and_exec_options_archive(self):
        self.options_archive = open(f'{sys.argv[2]}',"r+")
        for line in self.options_archive.readlines():

            if(line[0] == "i"):
                attributes = line[2:].strip().split(',')
                self.MySGBD_temp.set_register(dict(zip(self.MySGBD_temp.DB.fields,attributes))).write()

            if(line[0] == "d"):
                first_key = line[2:].strip()
                self.MySGBD_temp.delete(self.MySGBD_temp.grep_by_fk(first_key))

    def make_temp_archive(self):
        self.temp_archive = open(f'{sys.argv[3]}',"a+") #cria o arquivo caso não exista
        self.temp_archive.close()

        self.MySGBD_temp = SGBD().set_database_archive(f'{sys.argv[3]}')
        for register in self.MySGBD_input.read():
            self.MySGBD_temp.set_register(register).write()

    def make_output_archive(self):

        self.output_archive = open(f'{sys.argv[4]}',"a+") #cria o arquivo caso não exista
        self.output_archive.close()

        self.MySGBD_temp.DB.storage_compact(sys.argv[4])



run = AT2_Facade()

#Chamada via prompt
#python ED2-AT02-UpdateRegistros-HugoCarvalhoSerra.py input1.txt op1.txt temp1.txt output1.txt
from Libs.SGBD import SGBD
from Libs.Sorting import QuickSort,MergeSort,HeapSort,InsertionSort  
import sys

class AT03_Facade:

    def __init__(self):
        self.heroes_fields = ['Chave','Primeiro Nome', 'Sobrenome', 'Nome Herói', 'Poder', 'Fraqueza', 'Cidade', 'Profissão']
        self.validation()

    def validation(self):
        try:
            self.get_input_data()
            self.sorting()
            self.set_output_data()
        except Exception as e:
            open(sys.argv[2],'w').write('Arquivo Invalido!')
            print(e)

    def get_input_data(self):
        MySGBD_Input = SGBD(sys.argv[1]).set_fields(self.heroes_fields)
        self.data = MySGBD_Input.read()
        self.input_header = MySGBD_Input.Header()

        if(len(self.data) == 0):
            raise Exception('\nO arquivo de entrada esta vazio!')
        
        if(["SIZE", "TOP", "QTDE", "SORT", "ORDER"] != list(MySGBD_Input.Header().keys())):
            raise Exception('\nO Há algum problema com o cabeçalho!')
            
    def sorting(self):
        self.keys = [register['Chave'] for register in self.data]
        self.data = {register['Chave']:register for register in self.data}
        
        if(self.input_header['SORT']=='Q'):
            self.keys = QuickSort(self.keys).array
            return
        elif(self.input_header['SORT']=='M'):
            self.keys = MergeSort(self.keys).array
            return
        elif(self.input_header['SORT']=="H"):
            self.keys = HeapSort(self.keys).array
            return
        elif(self.input_header['SORT']=='I'):
            self.keys = InsertionSort(self.keys).array
            return
                   
        raise Exception('\nOs parametros de ordenação são invalidos!')

    def set_output_data(self):
        MySGBD_OutPut = SGBD(sys.argv[2]).set_fields(self.heroes_fields)
        MySGBD_OutPut.DB.Header['SORT'] = self.input_header['SORT']
        MySGBD_OutPut.DB.Header['ORDER'] = self.input_header['ORDER']
        MySGBD_OutPut.DB.update_header()

        if(self.input_header['ORDER']=='C'):
            for key in self.keys:
                MySGBD_OutPut.set_register(self.data[key]).write()
        elif(self.input_header['ORDER']=='D'):
            for key in reversed(self.keys):
                MySGBD_OutPut.set_register(self.data[key]).write()
        else:
            raise Exception("\nOs parametros de ordenação são invalidos!")        

#teste.py Data/AT03CasosDeTeste/input8.txt output.txt
run = AT03_Facade()
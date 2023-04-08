import sys
from random import randint
import time

class InputFile:

    def __init__(self,archive_name):
        self.archive = None
        self.archive_name = archive_name
        self.validation_status = "passed";


    def validate(self):

        self.check_if_exist()
        self.check_if_not_empty()
        self.check_first_param()
        self.check_second_param()

        if(self.validation_status == "passed"):
            return True
        else:
            self.archive = None
            return False


    def check_if_exist(self):
        if(self.validation_status != "passed"):
            return False

        try:
            archive = open(self.archive_name,'r')
            self.archive = archive
        except Exception as e:
            self.validation_status = "The chosen file does not exist."


    def check_if_not_empty(self):
        if(self.validation_status != "passed"):
            return False

        if(not self.archive.read()):
            self.validation_status = "The file appears to be empty."

        self.archive.seek(0, 0)


    def check_first_param(self):
        if(self.validation_status != "passed"):
            return False

        first_line = self.archive.readline()
        try:
            first_line = int(first_line)
        except Exception as e:
            self.validation_status = "The first parameter must be an integer"


    def check_second_param(self):
        if(self.validation_status != "passed"):
            return False

        second_line = self.archive.readline()
        if(not second_line):
            self.validation_status = "The second parameter has not been defined."
            return False

        if(len(second_line) > 2):
            self.validation_status = "The second parameter needs to be char type."
            return False

        if(not (second_line[0] == 'c' or second_line[0] == 'd' or second_line[0] == 'r')):
            self.validation_status = "The second parameter must be equal to 'c', 'd', or 'r'."


    def archive_reseted(self):
        self.archive.seek(0, 0)
        return self.archive


    def get_first_param(self):
        if(self.validation_status == "passed"):
            return int(self.archive_reseted().readlines()[0])


    def get_second_param(self):
        if(self.validation_status == "passed"):
            return self.archive_reseted().readlines()[1][0]

class OutputFile:

    def __init__(self):
        pass

class Sorting:
    def sort(self):
        self.time = time.time()
        if(self.option == "asc"):
            self.sort_asc()
        else:
            self.sort_desc()
        self.time = round((time.time() - self.time)*1000)

class InsertionSort(Sorting):

    def __init__(self,array,option='asc'):
        super()
        self.array = array
        self.length = len(array)
        self.option = option
        self.count = 0
        self.time = 0
        self.sort()

    def sort_asc(self):
        for i in range(1,self.length):
            aux = self.array[i]
            j = i-1
            while(j >= 0 and aux < self.array[j]):
                self.array[j+1] = self.array[j]
                self.count += 1
                j -= 1
            self.array[j+1] = aux

class SortAlgoritms:

    def __init__(self,lenght,option):
        self.lenght = lenght
        self.array = self.set_array_with_generate_options(option)
        self.run_all_sort_algoritms()

    def set_array_with_generate_options(self,option):
        if(option == "c"):
            return [x for x in range(1,self.lenght+1)]
        elif(option == "d"):
            return [x for x in range(self.lenght,0,-1)]
        elif(option == "r"):
            return [randint(0,32000) for x in range(1,self.lenght)]

    def run_all_sort_algoritms(self):

        self.insertion_sort = InsertionSort(self.array)
        # print(self.insertion_sort.array)
        print(self.insertion_sort.count)
        print(self.insertion_sort.time)
        # # self.selection_sort = SelectionSort(self.array)
        # # self.bubble_sort    = BubbleSort(self.array)
        # self.merge_sort     = MergeSort(self.array)
        # self.quick_sort     = QuickSort(self.array)
        # # self.heap_sort      = HeapSort(self.array)

class Main:

    def __init__(self):
        self.start()


    def start(self):
        input_file = InputFile(sys.argv[1])
        if(input_file.validate()):
            SortAlgoritms(input_file.get_first_param(), input_file.get_second_param())
        else:
            print(input_file.validation_status)




MainOBJ = Main()

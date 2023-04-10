import sys
from random import randint
import time

class InputFile:

    def __init__(self):
        self.validation_status = "passed";
        self.archive = None
        self.archive_name = None

    def validate(self):

        self.check_argv_input()
        self.check_if_exist()
        self.check_if_not_empty()
        self.check_first_param()
        self.check_second_param()

        if(self.validation_status == "passed"):
            return True
        else:
            self.archive = None
            print(self.validation_status)
            return False

    def check_argv_input(self):
        try:
            sys.argv[1]
            self.archive_name = sys.argv[1]
        except Exception as e:
            self.validation_status = "An input file is required."

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
        self.archive = None
        self.archive_name = None
        self.validation_status = "passed";

    def validate(self):
        self.check_argv_input()

        if(self.validation_status == "passed"):
            return True
        else:
            self.archive = None
            return False

    def generate(self,algorithms):

        if(self.validation_status == "passed"):
            for name,algorithm in algorithms.items():
                self.archive.writelines(f"{name}: {self.write_array(algorithm.array)}, {algorithm.count} comp, {algorithm.time_ms} ms \n")

    def generate_error(self,error):
        if(self.validation_status == "passed"):
            self.archive.writelines("Arquivo Invalido!")
        else:
            print(self.validation_status)


    def write_array(self,array):
        str = ""
        for element in array:
            str += f"{element} "
        return str[:-1]

    def check_argv_input(self):
        try:
            sys.argv[2]
            self.archive_name = sys.argv[2]
            self.archive = open(self.archive_name, 'w')
        except Exception as e:
            self.validation_status = "An output file is required."

class Sorting:

    def sort(self):
        self.time_ms = time.time()
        if(self.option == "asc"):
            self.sort_asc()
        else:
            self.sort_desc()# não implementado
        self.time_ms = round((time.time() - self.time_ms)*1000)

class BubbleSort(Sorting):

    def __init__(self,array,option='asc'):
        super()
        self.array = array
        self.length = len(array)
        self.option = option
        self.count = 0
        self.time_ms = 0
        self.sort()

    def sort_asc(self):
        if self.length == 1:
            return self.array

        for i in range(self.length):
            for j in range(self.length-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    self.count += 1

class InsertionSort(Sorting):

    def __init__(self,array,option='asc'):
        super()
        self.array = array
        self.length = len(array)
        self.option = option
        self.count = 0
        self.time_ms = 0
        self.sort()

    def sort_asc(self):
        if self.length == 1:
            return self.array

        for i in range(1,self.length):
            aux = self.array[i]
            j = i-1
            while(j >= 0 and aux < self.array[j]):
                self.array[j+1] = self.array[j]
                self.count += 1
                j -= 1

            self.array[j+1] = aux

class SelectionSort(Sorting):

    def __init__(self,array,option='asc'):
        super()
        self.array = array
        self.length = len(array)
        self.option = option
        self.count = 0
        self.time_ms = 0
        self.sort()

    def sort_asc(self):
        self.selection_sort(self.array,self.length)

    def selection_sort(self,array, n):

        if n == 1:
            return array

        minimo = 0
        for i in range(1, n):
            if array[i] < array[minimo]:
                minimo = i

        array[0], array[minimo] = array[minimo], array[0]

        self.selection_sort(array[1:], n-1)

class HeapSort(Sorting):

    def __init__(self,array,option='asc'):
        super()
        self.array = array
        self.length = len(array)
        self.option = option
        self.count = 0
        self.time_ms = 0
        self.sort()

    def sort_asc(self):
        self.heapSort(self.array)

    def heapSort(self,array):
        n = len(array)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(array, n, i)

        for i in range(n-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.count += 1
            self.heapify(array, i, 0)

    def heapify(self,array, n, i):
        maior = i
        L = 2 * i + 1
        R = 2 * i + 2

        if L < n and array[i] < array[L]:
            maior = L

        if R < n and array[maior] < array[R]:
            maior = R

        if maior != i:
            array[i],array[maior] = array[maior],array[i]
            self.count += 1
            self.heapify(array, n, maior)

class QuickSort(Sorting):

    def __init__(self,array,option='asc'):
        super()
        self.array = array
        self.length = len(array)-1
        self.option = option
        self.count = 0
        self.time_ms = 0
        self.sort()

    def sort_asc(self):
        self.quick_sort_first_pivot(self.array,0,self.length)

    def quick_sort_first_pivot(self, array, start, end):

        if(start < end):
            left, right, pivot = start, end, array[start]
            while(left < right):
                while(array[left] <= pivot and left < end):
                    left += 1

                while(array[right] > pivot and right >= start):
                    right -= 1

                if(left < right):
                    array[left], array[right] = array[right], array[left]
                    self.count += 1

            array[start], array[right] = array[right], array[start]
            self.count += 1

            self.quick_sort_first_pivot(array, start, right-1)
            self.quick_sort_first_pivot(array, right+1, end)
        self.array = array

class SortAlgorithms:

    def __init__(self,lenght,option):
        self.lenght = lenght
        self.array = self.set_array_with_generate_options(option)
        self.algorithms = {}
        self.run_all_sort_algoritms()

    def set_array_with_generate_options(self,option):
        if(option == "c"):
            return [x for x in range(1,self.lenght+1)]
        elif(option == "d"):
            return [x for x in range(self.lenght,0,-1)]
        elif(option == "r"):
            return [randint(0,32000) for x in range(1,self.lenght)]

    def run_all_sort_algoritms(self):

        self.algorithms['bubbleSort']    = BubbleSort(self.array.copy())
        self.algorithms['insertionSort'] = InsertionSort(self.array.copy())
        # self.algorithms['selectionSort'] = SelectionSort(self.array.copy())
        # self.algoritms['mergeSort']     = MergeSort(self.array)
        self.algorithms['quickSort']     = QuickSort(self.array.copy())
        self.algorithms['heapSort']      = HeapSort(self.array.copy())

class Main:

    def __init__(self):
        self.start()


    def start(self):
        input_file = InputFile()
        output_file = OutputFile()

        input_validate = input_file.validate()
        output_validate = output_file.validate()

        if(input_validate and output_validate):
            Sort = SortAlgorithms(input_file.get_first_param(), input_file.get_second_param())
            output_file.generate(Sort.algorithms)
        else:
            output_file.generate_error(input_file.validation_status)


MainOBJ = Main()

import sys
from random import randint
import time

sys.setrecursionlimit(100000)#tentativa de evitar erros de maximo de recursão


class Sorting:
    #está classe tem o objetivo de implementar a função sort e atributos comuns
    #em todas as classes que a herdarem. A função sort é chamada no construtor das classes filhas
    #e sempre fara a contagem do tempo de execução em milisegundos
    def __init__(self,array,option='asc'):
        self.array = array
        self.length = len(array)
        self.option = option
        self.count = 0
        self.time_ms = 0
        self.sort()

    def sort(self):
        self.time_ms = time.time()
        if(self.option == "asc"):
            self.sort_asc()
        else:
            self.sort_desc()# não implementado
        self.time_ms = round((time.time() - self.time_ms)*1000)


#todas as classes que herdam de Sorting, tem a mesma estrutura.
#os atributos são os dados necessarios para o preenchimento do arquivo de saida, herdados de Sorting
#e são preenchidos na execução da ordenação
#o metodo sort chamado no construtor é herdado de Sorting, e marca o tempo de execução

#o método sort_asc é uma fachada que abstrai as varias assinaturas diferentes dos metodos de
#ordenação implementados, para uma assinatura comum. Ou seja, para todos os metodos de ordenação
#chamar self.sort_asc() vai funcionar

class BubbleSort(Sorting):

    def __init__(self,array,option='asc'):
        super().__init__(array,option)

    def sort_asc(self):
        self.array = self.bubble_sort(self.array,len(self.array))

    def bubble_sort(self,array, n):

        #Se n == 1, significa que o array já está ordenado
        if n == 1:
            return array

        #Preferi a abordagem não recursiva pois a pilha de recursão do bubble sort é MUITO GRANDE
        for i in range(n):
            # Laço for que percorre o array e troca de lugar os elementos adjacentes caso o elemento à esquerda seja maior que o elemento à direita
            for j in range(n-1):
                self.count += 1
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
            n -= 1

        # Retorna o array ordenado
        return array


class InsertionSort(Sorting):

    def __init__(self,array,option='asc'):
        super().__init__(array,option)

    def sort_asc(self):
        #um array com apenas 1 elemento já esta ordenado
        if self.length == 1:
            return self.array

        #Laço externo que percorre o array
        for i in range(1,self.length):
            aux = self.array[i]
            j = i-1
            #Laço externo, se o elemento  i-1 for menor que o elemento i e i-1 maior que zero, entõo:
            while(j >= 0 and aux < self.array[j]):
                #desloca i-1 para i, abrindo espaço para inserir o elemento desordenado na posição correta
                self.array[j+1] = self.array[j]
                self.count += 1
                j -= 1

            #insere o elemento desordenado
            self.array[j+1] = aux


class SelectionSort(Sorting):

    def __init__(self,array,option='asc'):
        super().__init__(array,option)

    def sort_asc(self):
        self.array = self.selection_sort(self.array,self.length)

    def selection_sort(self,V, TAM):

        # O loop externo percorre a lista até a penúltima posição
        for N in range(TAM - 1):
            # Define a posição N como a posição atual do menor numero
            menor = N
             # O loop interno começa na posição seguinte a N e vai até o final da lista
            for i in range(N + 1, TAM):
                # Se o elemento atual for menor do que o elemento na posição do menor numero, atualiza o menor numero
                self.count += 1
                if V[i] < V[menor]:
                    menor = i
            # Se o menor numero não estiver na posição atual (ou seja, se houve uma troca), troca os valores
            if menor != N:
                V[N], V[menor] = V[menor], V[N]

        return V


class HeapSort(Sorting):

    def __init__(self,array,option='asc'):
        super().__init__(array,option)

    def sort_asc(self):
        self.heapSort(self.array)

    def heapSort(self,array):
        n = len(array)

        # Cria um heap máximo com o array
        # Inicia o loop pelo meio do array, que é a última posição que tem filhos
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(array, n, i)

        # Extrai o maior elemento do heap e coloca no final do array, repetindo até que todo o array esteja ordenado
        for i in range(n-1, 0, -1):
            # Troca o maior elemento, que é o primeiro do heap, com o último elemento não ordenado do array
            array[i], array[0] = array[0], array[i]
            # Reorganiza o heap para manter a propriedade de heap máximo
            self.heapify(array, i, 0)

    def heapify(self,array, n, i):
        maior = i# Inicia a posição atual como a maior posição
        L = 2 * i + 1# Calcula a posição do filho da esquerda
        R = 2 * i + 2# Calcula a posição do filho da direita

        # Se a posição do filho da esquerda é válida e o elemento na posição i é menor do que o elemento na posição L, atualiza a maior posição
        self.count += 1
        if L < n and array[i] < array[L]:
            maior = L

        # Se a posição do filho da direita é válida e o elemento na posição maior é menor do que o elemento na posição R, atualiza a maior posição
        self.count += 1
        if R < n and array[maior] < array[R]:
            maior = R

        # Se a maior posição não é mais a posição atual, troca os elementos e reorganiza o heap a partir da nova posição atual
        if maior != i:
            array[i],array[maior] = array[maior],array[i]
            self.heapify(array, n, maior)


class QuickSort(Sorting):

    def __init__(self,array,option='asc'):
        super().__init__(array,option)

    def sort_asc(self):
        self.quick_sort_first_pivot(self.array,0,self.length-1)

    def quick_sort_first_pivot(self, array, start, end):

        #se o array tiver tamanho diferente de 1, continua
        if(start < end):
            left, right, pivot = start, end, array[start]#definição dos index direito e esquerdo, e do pivo, no inicio do vetor
            while(left < right):#enquando os index não se "cruzarem", faça isso:

                #Encontra elementos maiores que o pivo, da esquerda para a direita
                while(array[left] <= pivot and left < end):
                    left += 1
                    self.count += 1

                #Encontra elementos menores que o pivo, da direita para a esquerda
                while(array[right] > pivot and right >= start):
                    right -= 1
                    self.count += 1

                #Caso o elemento encontrado estiver posicionado do lado errado do pivo, troca-os
                if(left < right):
                    array[left], array[right] = array[right], array[left]

            #poe o pivo na posição correta
            array[start], array[right] = array[right], array[start]
            self.count += 1

            #chamada recursiva para os 2 sub vetores, a esquerda e a direita do pivo
            self.quick_sort_first_pivot(array, start, right-1)
            self.quick_sort_first_pivot(array, right+1, end)
        self.array = array


class MergeSort(Sorting):

    def __init__(self,array,option='asc'):
        super().__init__(array,option)

    def sort_asc(self):
        self.array = self.merge_sort(self.array)

    def merge(self,left, right):
        left_index = right_index = 0
        array_aux = []

        #enquando index esquerdo for menor que a porção esquerda do array, e
        #enquando index direito for menor que a porção direita do array, faça:
        while left_index < len(left) and right_index < len(right):

            #se um elemento da porção esquerda, for menor que outro da porção direita
            self.count += 1
            if left[left_index] < right[right_index]:
                #salva o elemento no array auxiliar
                array_aux.append(left[left_index])
                left_index += 1
            else:#se um elemento da porção direita, for menor que outro da porção esquerda
                array_aux.append(right[right_index])#salva o menor no array auxiliar
                right_index += 1

        #concatena o array auxiliar, (que tem elementos menores) com o resto de left e right, que podem ter os elementos maiores que sobraram
        array_aux += left[left_index:]
        array_aux += right[right_index:]
        return array_aux

    def merge_sort(self,array):
        if len(array) <= 1:#Caso base
            return array

        #Divide o array em left e right recursivamente.
        mid  = len(array) // 2
        left  = self.merge_sort(array[:mid])
        right = self.merge_sort(array[mid:])

        #Ordena o vetor na volta da recursão
        return self.merge(left, right)


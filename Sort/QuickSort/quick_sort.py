from random import randint
import time

class QuickSort:

    def __init__(self,option="crescente",pivotChoice="random"):
        self.option = option
        self.pivotChoice = pivotChoice

    def sort_first(self, array, start, end):
        if(start < end):
            left, right, pivot = start, end, array[start]
            while(left < right):
                while(array[left] <= pivot and left <= end):
                    left += 1

                while(array[right] > pivot and right >= start):
                    right -= 1

                if(left < right):
                    array[left], array[right] = array[right], array[left]

            array[start], array[right] = array[right], array[start]
            self.sort_first(array, start, right-1)
            self.sort_first(array, right+1, end)
        self.array = array

    def sort_random(self, array, start, end):
        if(start < end):
            pivot_index = randint(start,end)
            left, right, pivot = start, end, array[pivot_index]
            print(f"pivo {pivot}")
            while(left < right):
                while(array[left] < pivot and left <= end):
                    left += 1

                while(array[right] > pivot and right >= start):
                    right -= 1

                print(f"{left} {right}")
                if(left <= right):
                    array[left], array[right] = array[right], array[left]
                    print(array)
                    print("TROCA")

                print("\n")
            array[left], array[pivot_index] = array[pivot_index], array[left]

            print(array)


            self.sort_random(array, start, pivot_index-1)
            self.sort_random(array, pivot_index+1, end)
        self.array = array

    def sort_last(self, array, start, end):
        if(start < end):
            left, right, pivot = start, end-1, array[end]
            while(left < right):
                while(array[left] < pivot and left <= end):
                    left += 1

                while(array[right] > pivot and right >= start):
                    right -= 1

                if(left < right):
                    array[left], array[right] = array[right], array[left]

            array[end], array[left] = array[left], array[end]
            self.sort_last(array, start, left-1)
            self.sort_last(array, left+1, end)
        self.array = array

    def compare(self):

        pivot_first_time_exec = 0
        pivot_random_time_exec = 0
        pivot_last_time_exec = 0

        for iteration in range(0,500):
            random_array = [randint(0,100) for i in range(0,500)]

            pivot_first_time_exec_start = time.time()
            self.pivotChoice = "first"
            self.sort(random_array)
            pivot_first_time_exec += time.time() - pivot_first_time_exec_start

            pivot_random_time_exec_start = time.time()
            self.pivotChoice = "random"
            self.sort(random_array)
            pivot_random_time_exec += time.time() - pivot_random_time_exec_start

            pivot_last_time_exec_start = time.time()
            self.pivotChoice = "last"
            self.sort(random_array)
            pivot_last_time_exec += time.time() - pivot_last_time_exec_start


        pivot_first_time_exec = pivot_first_time_exec
        pivot_random_time_exec = pivot_random_time_exec
        pivot_last_time_exec = pivot_last_time_exec

        print("{:.40f}".format(pivot_first_time_exec))
        print("{:.40f}".format(pivot_random_time_exec))
        print("{:.40f}".format(pivot_last_time_exec))


QuickSort = QuickSort(pivotChoice='random')
QuickSort.sort_random([5,2,8,4,3,1,9,6,7],0,8) #pivo = 3
print(QuickSort.array)

#[5, 2, 8, 4, 3, 1, 9, 6, 7]
#[5, 2, 1, 4, 6, 8, 9, 3, 7]

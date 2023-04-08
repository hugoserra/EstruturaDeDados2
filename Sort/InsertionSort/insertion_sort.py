class InsertionSort:

    def __init__(self,array,option='asc'):
        self.array = array
        self.length = len(array)
        self.option = option
        self.count = 0
        self.sort_all_step()
        print(self.array)
        print(self.count)

    def sort_all_step_asc(self):
        for i in range(1,self.length):
            aux = self.array[i]
            j = i-1
            while(j >= 0 and aux < self.array[j]):
                self.array[j+1] = self.array[j]
                self.count += 1
                print(self.array)
                j -= 1

            self.array[j+1] = aux

    def sort_all_step_desc(self):
        for i in range(1,self.length):
            aux = self.array[i]
            j = i-1
            while(j >= 0 and aux > self.array[j]):
                self.array[j+1] = self.array[j]
                j -= 1

            self.array[j+1] = aux

    def sort_all_step(self):
        if(self.option == "asc"):
            self.sort_all_step_asc()
        else:
            self.sort_all_step_desc()

InsertionSort([5,1,2,3,4,0],'asc')

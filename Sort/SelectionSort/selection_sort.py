class SelectionSort:

    def __init__(self,array,option='asc'):
        self.array = array
        self.length = len(array)
        self.option = option
        self.min_index = 0;
        self.start_index = 0;
        self.count = 0
        self.sort_all_steps()
        print(self.array)
        print(self.count)

    def sort_one_step_asc(self):
        self.min_index = self.start_index
        for i in range(self.start_index,self.length):
            if(self.array[i] < self.array[self.min_index]):
                self.min_index = i

        self.swap()

    def sort_one_step_desc(self):
        self.min_index = self.start_index
        for i in range(self.start_index,self.length):
            if(self.array[i] > self.array[self.min_index]):
                self.min_index = i

        self.swap()

    def swap(self):
        self.array[self.start_index],self.array[self.min_index] = self.array[self.min_index],self.array[self.start_index]
        self.start_index += 1
        self.count += 1

    def sort_all_steps(self):
            if(self.option == 'asc'):
                while(self.start_index < self.length-1):
                    self.sort_one_step_asc()
            else:
                while(self.start_index < self.length-1):
                    self.sort_one_step_desc()

SelectionSort([34, 38, -22, 29, 50, 33, 11, -19,  7, -29, -44, -49, -30, 32, -28],'asc')

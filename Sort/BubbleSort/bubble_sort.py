class BubbleSort:

    def __init__(self,array,option='asc'):
        self.run = True #condição de parada
        self.array = array
        self.length = len(array)
        self.option = option
        self.count = 0
        self.sort_all_steps()
        print(self.array)
        print(self.count)

    def sort_one_step_asc(self):
        self.run = False;
        for i in range(0,self.length-1):
            if(self.array[i]>self.array[i+1]):
                self.swap(i)

    def sort_one_step_desc(self):
        self.run = False;
        for i in range(0,self.length-1):
            if(self.array[i]<self.array[i+1]):
                self.swap(i)

    def swap(self,i):
        self.array[i],self.array[i+1] = self.array[i+1],self.array[i]
        self.run = True;
        self.count += 1

    def sort_all_steps(self):
            if(self.option == 'asc'):
                while self.run:
                    self.sort_one_step_asc()
            else:
                while self.run:
                    self.sort_one_step_desc()

BubbleSort([34, 38, -22, 29, 50, 33, 11, -19,  7, -29, -44, -49, -30, 32, -28],'asc')

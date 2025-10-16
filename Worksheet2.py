class Iteration:
    def __init__(self):
        self.data=[]
        self.size=100
    
    def initialise(self):
        self.data=sample(range(1,3*self.size),self.size)
    
    def __str__(self):
        output = f"Befor sorting the array is {self.data}"
        return output

def selection_sort(data):
    
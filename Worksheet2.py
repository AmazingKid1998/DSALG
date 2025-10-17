from random import sample
class Iteration:
    def __init__(self):
        self.data=[]
        self.size=10
    
    def initialise(self):
        self.data=sample(range(1,3*self.size),self.size)
    
    def __str__(self):
        output = f"The array is {self.data}"
        return output

    def selection_sort(self):
        n=len(self.data)
        for i in range(n-1):
            smallest_idx=i
            for j in range(i+1,n):
                if self.data[j]<self.data[smallest_idx]:
                    smallest_idx=j
            
            if smallest_idx!=i:
                self.data[i],self.data[smallest_idx]=self.data[smallest_idx],self.data[i]
        
        return self.data
    
    def bubble_sort(self):
        n=len(self.data)
        flag = False
        while not flag:
            flag = True
            for j in range(n-1):
                if self.data[j]>self.data[j+1]:
                    self.data[j],self.data[j+1]=self.data[j+1],self.data[j]
                    flag = False
            n-=1
        
        return self.data
    
    def insertion_sort(self):
        n=len(self.data)
        
        for i in range(n):
            item_to_insert=self.data[i]
            index_hole=i
            while index_hole>0 and self.data[index_hole-1]>item_to_insert:
                self.data[index_hole]=self.data[index_hole-1]
                index_hole-=1
            self.data[index_hole]=item_to_insert
    
    def linear_search(self,item):
        n=len(self.data)
        for i in range(n):
            if self.data[i]==item:
                return i
        print("Not Found")
        return -1
    
    def binary_search(self,item):
        n=len(self.data)
        lower=0
        upper=n-1
        while lower<=upper:
            mid=(lower+upper)//2
            if self.data[mid]==item:
                return mid
            elif self.data[mid]<item:
                upper=mid-1
            else:
                lower=mid+1
        print("Not found")
        return -1

def tester():
    arr=Iteration()
    arr.initialise()
    print(arr)
    
    arr.bubble_sort()
    print(arr)
    
    ind=arr.binary_search(23)
    print(ind)
    
    
    
    
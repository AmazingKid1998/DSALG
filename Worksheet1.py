class Queue:
    def __init__(self,data):
        self.array = data
        self.head=0
        self.tail=-1
         
    def enqueue(self,item):
        self.array.append(item)
        
    
    def dequeue(self):
        if (len(self.array)>0):
            item=self.array[self.head]
            del self.array[self.head]
            
        else:
            print("Queue already empty")
    
    def peek(self):
        print(self.array[self.head])
    
    def length(self):
        return len(self.array)
    
    def __str__(self):
        output=""
        if (len(self.array)>0):
            output= f"This queue is:"
            for i in range(0,len(self.array)):
                output+= f" {self.array[i]} "
            
        else:
            output=f"The queue is empty"
            
        return output
    
class Stack:
    def __init__(self,data):
        self.data=data
        self.top=-1
    
    def push(self,newData):
        self.data.append(newData)
    def pop(self):
        item=self.data[self.top]
        del self.data[self.top]
        return item
    def length(self):
        return len(self.data)
    def peek(self):
        print(self.data[self.top])
    def __str__(self):
        output=" "
        if (len(self.data)>0):
            output+= f"This stack is:"
            for i in range(0,len(self.data)):
                output+= f" {self.data[i]} "
            
        else:
            output+=f"The stack is empty"
            
        return output

def reverse_queue(queue):
    queue1=Queue([])
    stack1=Stack(queue)
    while stack1.length()>0:
        item=stack1.pop()
        queue1.enqueue(item)
    
    
    print(queue1)

class CircularQueue:
    def __init__(self,data):
        self.data=data
        self.head=0
        self.size=size
        self.tail=len(self.data)-1
    
    def enqueue(self,new_data):
        self.data.append(new_data)
        
        
    
            
    

def main():
    queue1=Queue([2,3])
    queue1.enqueue(6)
    queue1.enqueue(1)
    queue1.enqueue(2)
    
    print(queue1)
    
    reverse_queue(queue1.array)
main()
        
        
class Stack:
    def __init__(self,size):
        self.data=[]
        self.top=-1 #the top index is -1 so that after the first push it becomes 0 and points to the first element of the stack
        self.size=size
    
    def push(self,new_data):
        if self.top<self.size:
            self.data.append(new_data)
            self.top+=1
        else:
            raise OverflowError(f"Stack Already Full")
    
    def pop(self):
        if self.top>=0:
            popped_item=self.data[self.top]
            del self.data[self.top]
            self.top-=1
            return popped_item
        else:
            raise IndentationError(f"The stack is empty!")
    
    def peek(self):
        if self.top>=0:
            #print(f"{self.data[self.top]}")
            return self.data[self.top]
        else:
            raise IndentationError(f"The stack is empty")
    
    def length(self):
        #print(f"Length is {self.top+1}")
        return self.top + 1
        

def stack_tester():
    stack1=Stack(10)
    stack1.push(5)
    stack1.push(7)
    print(stack1.data)
    stack1.pop()
    #stack1.pop()
    #stack1.pop()
    print(stack1.data)
    

class Queue:
    
    def __init__(self,size):
        self.data=[]
        self.size=size
        self.head=0
        self.tail=-1
        
    def enqueue(self,new_data):
        if self.tail<self.size:
            self.data.append(new_data)
            self.tail+=1
        else:
            print(f" Queue Already full")
            
    def dequeue(self):
        if self.tail<self.head:
            item=self.data[self.head]
            del self.data[self.head]
            self.head+=1
            
            return item
        else:
            print(f"The queue is empty")
    
    def length(self):
        print (f"The length is {self.tail+1}")
    
    def peek(self):
        if self.tail>=0:
            print(f"{self.data[self.tail]}")
            return self.data[self.tail]
        else:
            print(f"The queue is empty")
        

class CircularQueue:
    def __init__(self,size):
        self.data=[None]*size
        self.size=size
        self.head=0
        self.tail=0
    
    def enqueue(self,new_data):
        if self.tail-self.head == self.size:
            raise OverflowError("Queue already full")
        new_index=self.tail % self.size
        self.tail+=1
        self.data[new_index]=new_data
    
    def dequeue(self):
        if self.tail==self.head:
            raise IndexError(f"Cannot delete from empty queue")
        new_index=self.head % self.size
        self.head+=1
        removed_item=self.data[new_index]
        #print(f"{removed_item}")
        return removed_item
        #del self.data[new_index]
    
    def peek(self):
        if self.tail==self.head:
            raise IndexError(f"Cannot peek from empty queue")
        new_index=self.head % self.size
        return self.data[new_index]
    
    def length(self):
        return self.tail-self.head
    
    def __str__(self):
        items=[]
        for i in range(self.head,self.tail):
            items.append(self.data[i%self.size])
        return f"Queue is {items}"
            

def circular_queue_tester():
    cq=CircularQueue(15)
    for i in range(15):
        cq.enqueue(i)
    
    print(cq)
    for i in range(10):
        cq.dequeue()
    print(cq)
    cq.enqueue(200)
    print(cq)


def remove_adjacent():
    text=input("Enter string: ")
    stack1=Stack(len(text))
    for i in text:
        if stack1.length()>1:
            if stack1.peek() == i :
                stack1.pop()
            else:
                stack1.push()
        
        else:
            stack1.push(i)
    
    print(stack1.data)

def valid_brackets():
    text=input("Enter string: ")
    words=Stack(len(text))
    brackets=Stack(len(text))
    left_brackets=['(','{','[']
    right_brackets=[')','}',']']
    for i in text:
        if i in left_brackets:
            brackets.push(i)
        elif (i == ']') and brackets.peek()=='[':
            brackets.pop()
        elif (i == '}') and brackets.peek()=='{':
            brackets.pop()
        elif (i == ')') and brackets.peek()=='(':
            brackets.pop()
        elif i in right_brackets :
            print("Unmatched right bracket")
            break
        else:
            words.push(i)
            
    if brackets.length() > 0:
        print("false")
    elif brackets.length()==0 and words.length()>0:
        print ("True")
    else:
        print("False")
        
        
    
    
    
    
            
        
        
        
            
        
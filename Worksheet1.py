class CircularQueue:
    def __init__(self,size):
        self.data=[None]*size
        self.size=size
        self.head=0
        self.tail=0
    
    def enqueue(self,new_data):
        if self.tail-self.head == self.size:
            raise OverflowError("Queue is full")
        new_index=self.tail%self.size
        self.data[new_index]=new_data
        self.tail+=1
    
    def dequeue(self):
        if self.head==self.tail:
            raise IndexError("Queue is empty")
        new_index=self.head%self.size
        removed_item=self.data[new_index]
        self.data[new_index]=None
        self.head+=1
        return removed_item
    
    def peek(self):
        if self.head==self.tail:
            raise IndexError("Queue is empty")
        return self.data[self.head % self.size]
    
    def length(self):
        return self.tail-self.head
    
    def __str__(self):
        output=f"The queue is: "
        for i in range(self.head,self.tail):
            output+=f"{self.data[i%self.size]}"
        
        return output
    

def circular_queue_tester():
    cq=CircularQueue(10)
    for i in range(10):
        cq.enqueue(i)
    
    cq.dequeue()
    cq.dequeue()
    cq.enqueue(15)
    
    print(cq)

#circular_queue_tester()

class Stack:
    def __init__(self,size):
        self.data=[None]*size
        self.size=size
        self.top=-1
    
    def push(self,new_data):
        if self.top+1==self.size:
            raise OverflowError("Stack is Full")
        self.top+=1
        self.data[self.top]=new_data
        
    def pop(self):
        if self.top==-1:
            raise IndexError("Stack is empty")
        item=self.data[self.top]
        self.data[self.top]=None
        self.top-=1
        return item
    
    def peek(self):
        if self.top==-1:
            raise IndexError("Stack is empty")
        return self.data[self.top]
    
    def length(self):
        return self.top+1
    
    def __str__(self):
        if self.top==-1:
            output=f"Stack is empty"
        else:
            output=f"The Stack is :"
            for i in range(self.top+1):
                output+=f" {self.data[i]} "
        return output

def stack_tester():
    stack1=Stack(10)
    for i in range(10):
        stack1.push(i)
    print(stack1)
    items=[]
    items.append(stack1.pop())
    print(items)
    print(stack1)

#stack_tester()

class Queue:
    def __init__(self,size):
        self.data=[None]*size
        self.size=size
        self.head=0
        self.tail=-1
    
    def enqueue(self,new_data):
        if self.tail+1==self.size:
            raise OverflowError("Queue full")
        self.tail+=1
        self.data[self.tail]=new_data
    
    def dequeue(self):
        if self.tail<self.head:
            raise IndexError("Queue empty")
        item=self.data[self.head]
        self.data[self.head]=None
        self.head+=1
        return item
    
    def length(self):
        return self.tail-self.head +1
    
    def peek(self):
        if self.tail<self.head:
            raise IndexError("queue empty")
        return self.data[self.head]
    
    def __str__(self):
        output=f"The Queue is : "
        if self.tail<self.head:
            output+=f"Empty"
        else:
            for i in range (self.head,self.tail+1):
                output+=f" {self.data[i]} "
        return output

def queue_tester():
    q1=Queue(5)
    for i in range(5):
        q1.enqueue(i)
    print(q1)
    q1.dequeue()
    print(q1)
    #q1.enqueue(6)
    #print(q1)

#queue_tester()

def remove_adjacent():
    text=input("Input String: ")
    stack1=Stack(len(text))
    for char in text:
        if  stack1.length()>0 and stack1.peek() == char:
            stack1.pop()
        else:
            stack1.push(char)
    
    print(stack1.data)

#remove_adjacent()

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
    
        
    
        
        
    

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
        self.head+=1
        return removed_item
    
    def peek(self):
        if self.head==self.tail:
            raise IndexError("Queue is empty")
        return self.data[self.tail % self.size]
    
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
        self.data=[]
        self.size=size
        self.top=-1
    
    def push(self,new_data):
        if self.top<self.size:
            self.data.append(new_data)
            self.top+=1
        else:
            raise OverflowError("Stack is Full")
    def pop(self):
        if self.top<0:
            raise IndexError("Stack is empty")
        item=self.data[self.top]
        del self.data[self.top]
        self.top-=1
        return item
    
    def peek(self):
        if self.top<0:
            raise IndexError("Stack is empty")
        return self.data[self.top]
    
    def length(self):
        return self.top+1

def stack_tester():
    stack1=Stack(10)
    for i in range(10):
        stack1.push(i)
    print(stack1.data)
    items=[]
    items.append(stack1.pop())
    print(items)
    print(stack1.data)

#stack_tester()

class Queue:
    def __init__(self,size):
        self.data=[]
        self.size=size
        self.head=0
        self.tail=-1
    
    def enqueue(self,new_data):
        if self.tail==self.size:
            raise OverflowError("Queue full")
        self.data.append(new_data)
        self.tail+=1
    
    def dequeue(self):
        if self.tail-self.head<=0:
            raise IndexError("Queue empty")
        item=self.data[self.head]
        self.head+=1
        return item
    
    def length(self):
        return self.tail-self.head
    
    def peek(self):
        if self.head ==self.tail:
            raise IndexError("queue empty")
        return self.data[self.tail]
    
    def __str__(self):
        output=f"The Queue is :"
        for i in range(self.head,self.tail+1):
            output+=f" {self.data[i]} "
        return output

def queue_tester():
    q1=Queue(5)
    for i in range(5):
        q1.enqueue(i)
    print(q1)
    q1.dequeue()
    print(q1)
    q1.enqueue(6)
    print(q1)

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
    
        
    
        
        
    

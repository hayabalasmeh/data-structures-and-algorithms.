




from _pytest.python_api import raises


class StackIsEmptyException(Exception):
    
    def __init__(self,*arg):
        if arg:
            self.message = arg[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return self.message
        else:
            return " StackIsEmptyException has been raised ! "

class QueueIsEmptyException(Exception):
    
    def __init__(self,*arg):
        if arg:
            self.message = arg[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return self.message
        else:
            return " QueueIsEmptyException has been raised ! "


class Node:
    """
    construct a node object with the value passed and a next pointer to the next node
    """
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
        
class Stack:
    def __init__(self):
        self.top = None

    def push(self,value):
        """
        create a node with a passed value and push this node to the top of the stack
        """
        #First Step: creation of new node with the passed value
        node = Node(value)
        
        #Second Step: to make the new node next pointer to point to whatever the top is pointing to .
        node.next = self.top

        #Third Step: make the top pointer to point to the new node 
        self.top = node

    
    def pop(self):
        """
        return the value of the node that the top pointer was pointing to, and remove this node from the stack
        """
        #speical case: in case the stack was empty it will raise an exception
        if self.top == None:
            raise StackIsEmptyException('Hey I cannot do the pop, stack is empty !')

        #Frist Step: Assign a variable to point to whatever the top pointer is pointing to
        prev = self.top

        #Second Step: Point the top pointer to point to whatever the variable next pointer(next pointer of the top pointer) is pointing to
        self.top = prev.next

        #Third Step:make the next pointer of the avriable to point to none and return the value of the removed node (prev)
        prev.next = None

        return prev.value

    
    def peek(self):
        """
        will take a look at what the top pointer is pointing and return its value without modifying the stack """
        if self.top == None:
            raise StackIsEmptyException('Hey I cannot peek, stack is empty !')
        return self.top.value

    def is_empty(self):
        """
        will ckeck if the stack is empty or not by checking if the top pointer is pointing to none or not
        """
        return not self.top



class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    """
    with th queue we have two pointers the front and rear 
    """
    def enqueue(self,value):
        """
        will create a new node with the value passed and it will be added to the rear of the queue"""

        #first Step: Creation of new node with the passed value
        node = Node(value)

        ## Then we need to make sure that the queue is not empty as in this case the addition will be different
        if self.front == None :
            """
            in this case I will make the front and rear pointing to the new node 
            """
            self.front = node
            self.rear = node
            return
      

        #second step: make the last node next pointer to point to the new node (rear.next) as it was pointing to null
        self.rear.next = node

        #third step: make the rear pointer points to the new node
        self.rear = node

    def dequeue(self):
        """
        remove the first node from the front (first in first out) and return its value and make the front pointer poits to the next node in that line"""
        
        #speical case: in case the queue was empty it will raise an exception
        if self.front == None:
            raise QueueIsEmptyException('Hey I cannot dequeue, queue is empty !')


        #first step: make a temporary refrence that point to whatever the front is pointing to
        temp = self.front

        #second step: make the front pointer points to the next node which will be accessed through the next pointer of temp
        self.front = temp.next

        #third step : make the next pointer of the removed node (temp) to point to none as for garpage collecter and finally return the value of the removed node
        temp.next = None

        return temp.value
    
    def peek(self):
        """
        will take a look at what the front pointer is pointing and return its value without modifying the queue """
        if self.front == None:
            raise QueueIsEmptyException('Hey I cannot peek, queue is empty !')
        return self.front.value

    def is_empty(self):
        """
        will ckeck if the queue is empty or not by checking if the front pointer is pointing to none or not
        """
        if (self.front and not self.rear) or (not self.front and self.rear):
            raise QueueIsEmptyException('For sure the queue you have is not Normal XD')

        return not self.front
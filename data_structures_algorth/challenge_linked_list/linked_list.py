

#node class in order to have values and pointer to next values

#from _typeshed import Self


from _typeshed import Self
from typing import Counter


class Node: # its has two thing associated with it the the data(values) and the pointer for the next value
    def __init__(self,value = '' ):
        self.value = value
        self.next= None # in ordder to be able to create node without data 
    
    def __str__(self):
        return str(self.value)




class LinkedList():
    
    def __init__(self):
        self.head = None

    all_values = 0
    #insert method to insert new node with a value to the head of the link list and it take three step:
    # 1- instantiation of new node with the value neing passed, 2-checking if header is pointing to first value then to make the next value pointer point to the header value which will be our next value after creation on new node 3- make the header pointing to the new node value
    def insert(self,value):

        

        #instanitation of node to pass the value to it in order to  added to it
        node = Node(value)
        
        #to point the next value pointer to the next value which is the current value of the head but first need to check if the head is created meaning is pointning to vlue as if not I can't decide which is the next value yet
        if self.head:
            node.next = self.head
        
        # we want the head to inhirit the attributes of the node instance as self.head.value and self.head.next attributes
        self.head = node

        #updating 
       # it suppose to return nothing only inserting value
    
     # checking if a value does exist inside the 

    def __iter__(self):

        current = self.head

        while current : #as to stop traversing when the  node is null

           yield current.value #will stop the function and send the node to the caller then make the function complete from where it stopped
        #    self.all_values = self.all_values +1
           current = current.next
    
    def includes(self,value):
        
        nodes = self.__iter__()

        if value in nodes:
            return True

        else:
            return False
        
    def __str__(self):
        nodes = self.__iter__()
        string = ""
        for value in nodes:
            string = string + f"{ {value} } -> "
        string = string + " Null"
        return string

    def append(self,value):

        node = Node(value)

        if self.head == None:
            
           self.head = node 
        
           return #in order to stop here in first time 
        current = self.head # to tranverse through the list

        while current.next: 
            current = current.next  #to tranverse through the nex until reach the null
        
        current.next = node # when the current.next equal to none assign the new obj to it

        

    def add_after(self,value,new_value):
        node = Node(new_value)
        
        # if self.head == None:
        #     self.head = node
        
        
        current = self.head
        
        while current.next: 
         #to tranverse through the nex until reach the value
            if (current.value == value):
                #first you need to keep the refrence for the next node
                node.next = current.next
                current.next  =  node
                # when the current.next equal to none assign the new obj to it
                break
            current = current.next     
       
        
    def add_before(self,value,new_value):
        node = Node(new_value)
        case = False
        current = self.head
        prev = self.head
        if(self.head == None):
            next_node = Node(value)
            self.head = node
            node.next = next_node
            
        while current: 
           
           
         #to tranverse through the nex until reach the value
            if(current.value == value):
                prev.next = node
                node.next = current
                case = True
                break
                # when the current.next equal to none assign the new obj to it
                # return
            prev = current
            current = current.next 

    def get_kth_value(self,k):
        nodes = self.__iter__() 
        total = 0
        for i in nodes:
            total = total + 1
        counter_list = total -1
        
        
        if self.head == None:
            raise Exception('The node list is Empty')

        if k > counter_list or k < 0:
            raise Exception('You are out of Range')
        
            
        current = self.head
        while (counter_list >= 0):
            if counter_list == k:
              return current.value
            counter_list =counter_list-1  
            current = current.next
        raise Exception('The value does not exist')
        
    def linked_list_zip(self,link_list_one,link_list_two):
       
    #    new_list = LinkedList()
       
    #    new_list.self.insert(link_list_one.head.value)
       node = Node(0)
       self.head = node 
       
       current = self.head
       while current.next:
           


    # good representation of all the values(nodes) inside the linked list
    # representation of the linked list
    def __repr__(self):
        return "LinkedList"

if __name__ == '__main__' :
   num = LinkedList()
   num.insert(1)
#    num.insert(2)
#    num.insert(3)
   #node = Node(1)
#    print(num.includes(7))
   print(num.get_kth_value(0))
  

#    integ = Linked_list()
#    integ.insert(5)
#    integ.insert(7)
   
#    print(integ.includes(5)) 
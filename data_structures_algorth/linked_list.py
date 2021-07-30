

#node class in order to have values and pointer to next values

#from _typeshed import Self


class Node:
    def __init__(self,value='' ):
        self.value = value
        self.next= None
    
    




class Linked_list:
    
    def __init__(self):
        self.head = None

    all_values = []
    #insert method to insert new node with a value to the head of the link list and it take three step:
    # 1- instantiation of new node with the value neing passed, 2-checking if header is pointing to first value then to make the next value pointer point to the header value which will be our next value after creation on new node 3- make the header pointing to the new node value
    def insert(self,value):

        

        #instanitation of node to pass the value to it in order to  added to it
        node = Node(value)
        
        #to point the next pointer to the next value which is the current value but first need to check if the head is created meaning is pointning to vlue as if not I can't decide whic is the next value yet
        if self.head:
            node.next = self.head
        
        # we want the head to point to the new node value as the first value 
        self.head = node.value

        #updating 
       # it suppose to return nothing only inserting value
    
     # checking if a value does exist inside the 
    
    def includes(self,value):
        if self.head == value:
           
            return True
        else:
            return False

  
    

    # good representation of all the values(nodes) inside the linked list

if __name__ == '__main__' :
   num = Linked_list()
   num.insert(1)
   num.insert(2)
   num.insert(3)
   print(num.includes(3))

   integ = Linked_list()
   integ.insert(5)
   integ.insert(7)
   
   print(integ.includes(5)) 
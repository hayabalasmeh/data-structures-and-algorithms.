# Building the class

class Node:

    def __init__(self,value = ''):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedListInsertion:

    def __init__(self):
       self.head = None 



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
      
        if self.head == None:
            self.head = node
            
        
        current = self.head

        holder = None
        
        while current.next: 
            holder = current
           
         #to tranverse through the nex until reach the value
            if (holder.value == value):
                node.next = current.next
                holder.next  =  node
                # when the current.next equal to none assign the new obj to it
                return
            current = current.next     
        
    def add_before(self,value,new_value):
        node = Node(new_value)
      
        if self.head == None:
            self.head = node
            
        
        current = self.head

        holder = None
        
        while current.value != value: 
            holder = current
           
         #to tranverse through the nex until reach the value
            # if (holder.value == value):
             
                # when the current.next equal to none assign the new obj to it
                # return
            current = current.next 
        if (current != None):
           node.next = holder.next
           holder.next  =  node
        
        
        
                        
        value = node

    def __iter__(self):

        current = self.head

        while current : #as to stop traversing when the  node is null

           yield current.value #will stop the function and send the node to the caller then make the function complete from where it stopped
           current = current.next

    def __str__(self):
        nodes = self.__iter__()
        string = ""
        for value in nodes:
            string = string + f"{ {value} } -> "
        string = string + " Null"
        return string

if __name__ == '__main__' :
        num = LinkedListInsertion()
        num.append(1)
        num.append(2)
        num.append(3)
        num.append(5)
        num.add_before(7,6)
        # num.add_before(3,4)
        print(num)
        print(num)    


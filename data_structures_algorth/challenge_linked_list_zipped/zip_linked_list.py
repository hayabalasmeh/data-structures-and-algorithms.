
from data_structures_algorth.challenge_linked_list.linked_list import  LinkedList


def linked_list_zip(link_list_one,link_list_two):
       
        first  = link_list_one.head
        second = link_list_two.head
       
        if link_list_one == None and link_list_two == None:
           raise Exception(RuntimeError,'Both lists are empty')
        if link_list_one.head == None:
          return link_list_two
        if link_list_two.head == None:
          return link_list_one
        # new_list = LinkedList() 1,2 ,7--- 3,4 --------- 1,3,2,4
        
        prev = None 
        tail = None
        

        while first and second :
            if first.next ==None:
                first.next = second
                break

            prev = first.next #store what head1 is pointing to n= 2
            tail = second.next## it's pointing to the forth node n=4
 
          
            second.next = prev # it's pointing to third node 1--3--2
            first.next = second # # it's pointing to second head 1-3
 
           
            first = prev  # update the first and second for next 
            second= tail
                
        return link_list_one   
        
          
if __name__ == '__main__' :
   num = LinkedList()
   num_2 = LinkedList()
   num_4 = LinkedList()
   num.insert(2)
   num.insert(1)
   num.insert(8)
#    num_2.insert(4)
   num_2.insert(3)
  
   print(linked_list_zip(num,num_2))
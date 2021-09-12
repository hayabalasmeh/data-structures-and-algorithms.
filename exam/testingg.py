from data_structures_algorth.challenge_linked_list.linked_list import LinkedList,Node
    
    
def removeNthFromEnd(listt, n: int):
        current = listt.head
        if current.next == None and n == 1:
            current = None
            return current

        counter = 0
        prev = None
        while current:
            counter += 1
            current = current.next

        current = listt.head
        while current :
            
            if counter == n:
                
                prev.next = current.next
                current.next = None
            counter = counter - 1
            prev = current
            current = current.next
        return listt

def mergeTwoLists( l1, l2):
        current_first = l1.head
        current_second = l2.head
        next_first = None
        next_second = None
        while current_first and current_second :
            if current_first.value < current_second.value: #1 < 2  # 3< 4
                next_first = current_first.next # 3 5
                next_second = current_second.next
                
                
                current_first.next = current_second #1--2 3--4
                if current_second.value < next_first.value:
                    current_second.next = next_first
                

                
                current_first = next_first #
                current_second = next_second
            else:
                next_first = current_first.next # 3 5
                next_second = current_second.next

                current_second.next = current_first # 1--2
                if next_second == None or current_first.value < next_second.value:
                    current_first.next = next_second
                
                
                current_first = next_first #
                current_second = next_second
        if l1.head.value < l2.head.value:
            return l1
        else:
            return l2

def duplicate(list):
    new_list = LinkedList()
    new_list.insert(0)
    new_head = new_list.head
    current = list.head
    while current:
        if current.next and current.value == current.next.value :
            while current.next and current.value == current.next.value:
                current = current.next
            new_head.next = current.next
        else:
            new_head.next = current
            
            new_head = new_head.next

            
        current = current.next
    new_list.head = new_list.head.next
    return new_list
def reverse_nth(left,right,head):
        counter = 0
        current = head.head
        next_val = None
        prev_val = None
        head_2 =None    
        while current:
            counter += 1
            if counter == left:
                big_curr = prev
                while not counter == right+1:
                    
                        
                    next_val = current.next
                    if not prev_val:
                        tail = current
                    current.next = prev_val
                    prev_val = current
                    current = next_val #7

                    
                    counter += 1
                big_curr.next = prev_val
                tail.next = current
        
            prev = current
            current = current.next
def find_shortest_path(linked_list, k):
    if not linked_list.head:
        return ' The are no such nodes resulting the kth'
    if not linked_list.head.next:
       if linked_list.head.value == k:
           return [ linked_list.head.value,0]
       else:
            return ' The are no such nodes resulting the kth'
    current = linked_list.head
    counter = 0
    list_values = []
    
    while current:
               current_value = current.value #1
               if current.next:
                current_inner = current.next #2
               counter = 0
               while current_inner: 
                    counter += 1
                    if (current_value + current_inner.value) == k:# 1+4
                                       
                                       if not list_values:

                                              list_values.append([current_inner.value,current_value,counter])
                                       else:
                                           if list_values[0][2] > counter:
                                                list_values.pop()
                                                list_values.append([current_inner.value,current_value,counter])
                                    
                                         
                    
                    current_inner = current_inner.next
                
               current = current.next
                          
    return list_values    

                
        # return head
if __name__=="__main__":
    on = LinkedList()
    # on.insert(8)
    # on.insert(7)
    on.insert(4)
    on.insert(3)
    on.insert(2)
    on.insert(1)
    on2 = LinkedList()
    on2.insert(6)
    on2.insert(5)
    on2.insert(3)
    on2.insert(3)
    on2.insert(2)
    on2.insert(2)
    on2.insert(1)
    # print(removeNthFromEnd(on,1))
    # print(duplicate(on2))
    # print(reverse_nth(2,5,on))
    print(find_shortest_path(on,5))

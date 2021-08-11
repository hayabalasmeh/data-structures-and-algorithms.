

from data_structures_algorth.challenge_stack_and_queue.stack_queue import Queue

def DuckDuckGoose(list,k):
   
    checker = Queue()
    checker_2 = Queue()
    counter = 0
    for i in list:
        counter = counter +1 # 1 , 2 , 3
        checker.enqueue(i) # A , B , D ,
        if counter == k: 
            checker.dequeue()
            counter = 0
        
         # A B C D inside Queue , k = 3 
        # while checker.front:
        # counter = 0
        # for i in range(k):
        #    if k -1 == i:
        #        checker.dequeue()
        # counter = 0
        # checker.front.next

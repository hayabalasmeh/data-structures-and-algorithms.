from data_structures_algorth.challenge_stack_and_queue.stack_queue import Stack
# from data_structures_algorth.challenge_pseudo_queue.pseudo_queue

class PseudoQueue:
    def __init__(self):
        self.front = Stack()
        self.rear = Stack()

    def enqueue(self,value):
        self.front.push(value)

    def dequeue(self):
        if self.rear.is_empty():
            while not self.front.is_empty():  
               removed = self.front.pop()
               self.rear.push(removed)

        
        return self.rear.pop()

        

if __name__ == '__main__':
    pseudo = PseudoQueue()
    pseudo.enqueue(1)
    pseudo.enqueue(2)
    pseudo.enqueue(3)
    pseudo.enqueue(3)
    pseudo.dequeue()
    print(pseudo.front.top.value)
    print(pseudo.rear.top.value)
    print(pseudo.dequeue())
    # print(pseudo.dequeue())
    # print(pseudo.dequeue())
    # print(pseudo.dequeue())
    # print(pseudo.dequeue())

    
    # print(pseudo)
    
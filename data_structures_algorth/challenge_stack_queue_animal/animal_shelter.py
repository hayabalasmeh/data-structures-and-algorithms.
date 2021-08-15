from data_structures_algorth.challenge_stack_and_queue.stack_queue import Queue, QueueIsEmptyException



class AnimalShelter:
    def __init__(self):
        """
        will construct 2 objects cat and dog as instances of queue class
        """
        self.dog = Queue()
        self.cat = Queue()
        

    def enqueue(self,animal):
        """
        will check first if the animal wanted to be added dog or cat and according to that it will add the animal to the animal shelter"""

        if animal == 'dog':
           self.dog.enqueue('dog')
        elif animal == 'cat':
            self.cat.enqueue('cat')
        else:
            raise Exception('No other animals are allowed!!')
    
    def dequeue(self,pref='none'):
        """
        will check first if the animal wanted to be removed from the shelter is dog or cat and remove it from the shelter in accordance to first in first out """
        
        #first check if the dog queue is not empty
        
        if pref == 'dog':
            if self.dog.front:
                return self.dog.dequeue()
            else:
                raise QueueIsEmptyException('Sorry there are no dogs waiting in our shelter')
                
        elif pref == 'cat':
            if self.cat.front:
                return self.cat.dequeue()
            else:
                raise QueueIsEmptyException('Sorry there are no cats waiting in our shelter')
                
        else:
            return None

if __name__== '__main__':
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('cat')
    
    print(shelter.dog.front.value)
    print(shelter.dog.rear.value)
    print(shelter.cat.front.value)
    print(shelter.cat.rear.value)
    shelter.dequeue('cat')
    shelter.dequeue('cat')
    # print(shelter.cat.front.value)
    print(shelter.dequeue('cat'))
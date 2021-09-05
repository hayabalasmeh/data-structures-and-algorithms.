
from data_structures_algorth.challenge_linked_list.linked_list import *

class HashTable:

    def __init__(self)-> None:
        """
        Constructs a Hash table object with a size of 200 buckets 

        """
        self.size = 200
        self.buckets = [LinkedList()] * self.size
    
    def hash(self,key:str)-> int:
        """
        Get the index of a specific given Key string
        Arguments:
        Key; string
        Return: index

        """
        #First we need to sum the ASCII code for all of the characters in the key 
        sum = 0
        for char in key:
            sum += ord(char)
        
        #Second we need to add a primer number to the maping relation 
        index = (sum * 9 )% self.size

        return index

    def add(self,key:str,value)-> None:
        """
        Add a value to the Hash table according to the key 
        Arguments:
        Key; string
        Value; any type
        Return: nothing

        """
        #First we need to get the index number
        index = self.hash(key)

        #Second I need to add the value and key to the linkedlist at this index
        
        
        self.buckets[index].append([key,value])

    def get(self,key:str):
        """
        Get the value stored by the given key
        Arguments; 
        Key; string
        Returns ; Value

        """
        index = self.hash(key)
        element = self.buckets[index].head
        while element:
            if element.value[0] == key:
                return element.value[1]
            element = element.next
        raise Exception( " No such key existed")

    def contains(self,key:str)-> bool:
        """
        Check if the given key is exited in the Hash table
        Arguments; Key: string
        Returns; Boolean
        
        """
        index = self.hash(key)
        element = self.buckets[index].head
        while element:
            if element.value[0] == key:
                return True
            element = element.next
        return False









if __name__=="__main__":
    # arr = [2]*3
    # print(type(arr[0]))
    obj = HashTable()
    obj.add('haya',2)
   
    index = obj.hash('haya')
    print(obj.buckets[0].head.value == 2)
    # print(obj.buckets[index].includes(2))
    print(obj.get('haya'))
    print(obj.contains('hi'))
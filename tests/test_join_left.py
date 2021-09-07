from data_structures_algorth.challenge_hashtable.hashtable import HashTable
from data_structures_algorth.challenge_hash_left_join.left_join import left_join

# Testing if joining all the left and matching right values

def test_joining():
    #Arrange
    hash_1 = HashTable()
    hash_1.add('nice','good')
    hash_1.add('small','tiny')
    
    hash_2 = HashTable()
    hash_2.add('small','big')
    hash_2.add('nice','bad')
    hash_2.add('old','new')
    
    #Act
    result = left_join(hash_1,hash_2)
    #Assert
    assert  result == [['small', 'tiny', 'big'], ['nice', 'good', 'bad']]

# Testing if Retrieving null value in case no matching of key occured in second hashmap

def test_adding_null_value():
    #Arrange
    hash_1 = HashTable()
    hash_1.add('nice','good')
    hash_1.add('small','tiny')
    hash_1.add('beautiful','sweet')
    hash_2 = HashTable()
    hash_2.add('small','big')
    hash_2.add('nice','bad')
    hash_2.add('old','new')
    
    #Act
    result = left_join(hash_1,hash_2)
    #Assert
    assert result == [['beautiful', 'sweet', 'Null'], ['small', 'tiny', 'big'], ['nice', 'good', 'bad']]

# Testing if the first hashmap was empty it return empty list

def test_empty_first_hashmap():
    #Arrange
    hash_1 = HashTable()
    hash_2 = HashTable()
    hash_2.add('small','big')
    hash_2.add('nice','bad')
    hash_2.add('old','new')
    
    #Act
    result = left_join(hash_1,hash_2)
    #Assert
    assert result == []

# Testing if the both hashmaps were empty it return empty list

def test_empty_both_hashmap():
    #Arrange
    hash_1 = HashTable()
    hash_2 = HashTable()
 
    #Act
    result = left_join(hash_1,hash_2)
    #Assert
    assert result == []

    
from data_structures_algorth.challenge_hashtable.hashtable import HashTable

# Testing if Adding a key/value to your hashtable results in the value being in the data structure

def test_adding():
    #Arrange
    test_obj = HashTable()
    index = test_obj.hash('test')
    #Act
    test_obj.add('test',5)
    #Assert
    assert  test_obj.buckets[index].head.value == ['test',5]

# Testing if Retrieving based on a key returns the value stored

def test_getting_value():
    #Arrange
    test_obj = HashTable()
    test_obj.add('test',5)
    #Act
    value = test_obj.get('test')
    #Assert
    assert value == 5

# Testing if Successfully returns false for a key that does not exist in the hashtable

def test_contain_key():
    #Arrange
    test_obj = HashTable()
    test_obj.add('test',5)
    #Act
    result = test_obj.contains('test_two')
    #Assert
    assert not result 

#Successfully retrieve a value from a bucket within the hashtable that has a collision

def test_handle_collision():
    #Arrange
    test_obj = HashTable()
    test_obj.add('test',5)
    test_obj.add('sett',9)
    #Act 
    sett_value = test_obj.get('sett')
    test_value = test_obj.get('test')
    #Assert
    assert sett_value == 9
    assert test_value == 5

#Successfully hash a key to an in-range value

def test_hash_in_range():
    #Arrange
    test_obj = HashTable()
    
    #Act 
    index = test_obj.hash('test')
    #Assert
    assert index in range(0,test_obj.size+1)
    
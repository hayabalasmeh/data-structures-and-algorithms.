
from data_structures_algorth.challenge_hashtable.hashtable import HashTable
from data_structures_algorth.challenge_hashmap_repeated.hashmap_repeated import find_repeated

#Can successfully return the first occurence of the word

def test_find_repeated():
    #ARRange
    string = "Once upon a time, there was a brave princess who..."
    #Act
    word = find_repeated(string)

    #Assert
    assert word == 'a'

#Can successfully return the first occurence of the word if it was  capitalized

def test_find_repeated_upper_case():
    #ARRange
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, "
    #Act
    word = find_repeated(string)

    #Assert
    assert word == 'it'

#Can successfully return the first occurence of the word if it has extra character

def test_find_repeated_extra_chara():
    #ARRange
    string = "It was a queer, sultry summer, the summer"
    #Act
    word = find_repeated(string)

    #Assert
    assert word == 'summer'

def test_find_repeated_return_empty():
    #Arrange
    string = "It was a queer, sultry the summer"
    #Act
    word = find_repeated(string)

    #Assert
    assert word == ''

#addressing the empty string
def test_find_repeated_check_empty():
    #Arrange
    string = ""
    #Act
    word = find_repeated(string)

    #Assert
    assert word == ''


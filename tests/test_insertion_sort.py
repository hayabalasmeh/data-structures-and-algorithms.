from data_structures_algorth.challenge_insertion_sort.insertion_sort import insertion_sort

# Testing when the list is empty it will return empty list
def test_insertion_sorting():
    #arrange
    arr = []
    expected = arr
    #Act
    actual = insertion_sort(arr)
    #Assert 
    assert expected == actual

# Testing when the list is has postive numbers
def test_insertion_sorting_positive():
    #arrange
    arr = [8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    #Act
    actual = insertion_sort(arr)
    #Assert 
    assert expected == actual

# Testing when the list is has negative numbers
def test_insertion_sorting_negative():
    #arrange
    arr = [20,18,12,8,-5,-2]
    expected = [-5,-2,8,12,18,20]
    #Act
    actual = insertion_sort(arr)
    #Assert 
    assert expected == actual
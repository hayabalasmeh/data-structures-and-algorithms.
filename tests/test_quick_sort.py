from data_structures_algorth.challenge_quick_sort.quick_sort import quicksort

# Testing when the list is empty it will return empty list
def test_quick_sorting():
    #arrange
    arr = []
    expected = arr
    #Act
    actual = quicksort(arr,0,0)
    #Assert 
    assert expected == actual

# Testing when the list is has postive numbers
def test_quick_sorting_positive():
    #arrange
    arr = [8,4,23,42,16,15]
    n = len(arr)
    expected = [4,8,15,16,23,42]
    #Act
    actual = quicksort(arr,0,n-1)
    #Assert 
    assert expected == actual

# Testing when the list is has negative numbers
def test_quick_sorting_negative():
    #arrange
    arr = [20,18,12,8,-5,-2]
    n = len(arr)
    expected = [-5,-2,8,12,18,20]
    #Act
    actual = quicksort(arr,0,n-1)
    #Assert 
    assert expected == actual
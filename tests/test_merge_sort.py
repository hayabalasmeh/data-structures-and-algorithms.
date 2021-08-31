from data_structures_algorth.challenge_merge_sort.merge_sort import mergesort

# Testing when the list is empty it will return empty list
def test_merging_sorting():
    #arrange
    arr = []
    expected = arr
    #Act
    actual = mergesort(arr)
    #Assert 
    assert expected == actual

# Testing when the list is has postive numbers
def test_merge_sorting_positive():
    #arrange
    arr = [8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    #Act
    actual = mergesort(arr)
    #Assert 
    assert expected == actual

# Testing when the list is has negative numbers
def test_merge_sorting_negative():
    #arrange
    arr = [20,18,12,8,-5,-2]
    expected = [-5,-2,8,12,18,20]
    #Act
    actual = mergesort(arr)
    #Assert 
    assert expected == actual
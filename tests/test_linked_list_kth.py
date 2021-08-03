
import pytest

from data_structures_algorth.challenge_linked_list.linked_list import LinkedList,Node

#Where k and the length of the list are the same
def test_same_length():
    result_2 = LinkedList()
    result_2.insert(5)
    result_2.insert(4)
    expected = result_2.get_kth_value(1)
    assert  expected == 4

def test_head_same_index():
    result_3 = LinkedList()
    result_3.insert(5)
    result_3.insert(4)
    expected = result_3.get_kth_value(0)
    assert  expected == 5
#Where k is greater than the length of the linked list
def test_out_range():
  try:
    result_1 = LinkedList()
    result_1.insert(5)
    result_1.insert(4)
    result_1.insert(3)
    result_1.get_kth_value(5)
  except Exception as e:
        print(e)
        assert str(e) == "You are out of Range"


#Where k is not a positive integer
def test_negative_index():
  try:
    result_4 = LinkedList()
    result_4.insert(5)
   
    result_4.get_kth_value(-1)
  except Exception as e:
        print(e)
        assert str(e) == "You are out of Range"

#Where the linked list is of a size 1
def test_length_one():
    result_5 = LinkedList()
    result_5.insert(5)
    
    expected = result_5.get_kth_value(0)
    assert  expected == 5
#  where k is not at the end, but somewhere in the middle of the linked list
def test_middle_index():
    result_6 = LinkedList()
    result_6.insert(5)
    result_6.insert(7)
    result_6.insert(2)
    result_6.insert(4)
    result_6.insert(3)
    expected = result_6.get_kth_value(2)
    assert  expected == 2
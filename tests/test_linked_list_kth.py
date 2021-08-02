
import pytest

from data_structures_algorth.challenge_linked_list.linked_list import LinkedList,Node

#Where k and the length of the list are the same
def test_same_length():
    result_2 = LinkedList()
    result_2.insert(5)
    result_2.insert(4)
    print(result_2.get_kth_value(1))
    assert  print(result_2.get_kth_value(1)) == 4
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
        assert str(e) == "You are out Range"


#Where k is not a positive integer
#Where the linked list is of a size 1
#  where k is not at the end, but somewhere in the middle of the linked list

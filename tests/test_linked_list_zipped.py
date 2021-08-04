
import pytest

from data_structures_algorth.challenge_linked_list.linked_list import LinkedList,Node

# test if the first list was empty it will return the second list :

def test_first_list_null():
   num = LinkedList()
   num_4 = LinkedList()
   num.insert(1)
   num.insert(2)
   num.insert(3)
  
   num_3 = LinkedList()
   expected = str(num_3.linked_list_zip(num,num_4))
   actual = '{3} -> {2} -> {1} ->  Null'
   assert actual == expected

# test if the second list was empty it will return the first list :
def test_second_list_null():
   num = LinkedList()
   num_4 = LinkedList()
   num.insert(1)
   num.insert(2)
   num.insert(3)
  
   num_3 = LinkedList()
   expected = str(num_3.linked_list_zip(num_4,num))
   actual = '{3} -> {2} -> {1} ->  Null'
   assert actual == expected

# test if both list were empty it will raise exception that the list is empty :
def test_both_list_null():
 try:
   num = LinkedList()
   num_4 = LinkedList()
   num_3 = LinkedList()
   num_3.linked_list_zip(num_4,num)
   
   
 except Exception as e:
        print(e)
        assert str(e) == 'empty list'
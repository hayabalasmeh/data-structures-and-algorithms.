
import pytest

from data_structures_algorth.challenge_linked_list.linked_list import LinkedList,Node
from data_structures_algorth.challenge_linked_list_zipped.zip_linked_list import linked_list_zip

# test if the first list was empty it will return the second list :

def test_first_list_null():
   num = LinkedList()
   num_4 = LinkedList()
   num.insert(1)
   num.insert(2)
   num.insert(3)
  
   
   expected = str(linked_list_zip(num,num_4))
   actual = '{3} -> {2} -> {1} ->  Null'
   assert actual == expected

# test if the second list was empty it will return the first list :
def test_second_list_null():
   num = LinkedList()
   num_4 = LinkedList()
   num.insert(1)
   num.insert(2)
   num.insert(3)
  
  
   expected = str(linked_list_zip(num_4,num))
   actual = '{3} -> {2} -> {1} ->  Null'
   assert actual == expected

# test if both list were empty it will raise exception that the list is empty :
def test_both_list_null():
 try:
   num = LinkedList()
   num_4 = LinkedList()
   
   linked_list_zip(num_4,num)
   
   
 except Exception as e:
        print(e)
        assert str(e) == 'empty list'
# if the first list has single node
def test_first_list_single_node():
   num = LinkedList()
   num_4 = LinkedList()
   num_4.insert(5)
   num.insert(1)
   num.insert(2)
   num.insert(3)
  
 
   expected = str(linked_list_zip(num_4,num))
   actual = '{5} -> {3} -> {2} -> {1} ->  Null'
   assert actual == expected

# if the second list has single node
def test_second_list_single_node():
   num = LinkedList()
   num_4 = LinkedList()
   num_4.insert(5)
   num.insert(1)
   num.insert(2)
   num.insert(3)
  
 
   expected = str(linked_list_zip(num,num_4))
   actual = '{3} -> {5} -> {2} -> {1} ->  Null'
   assert actual == expected
   
# test when the first list is shorter than the second
def test_first_list_short():
   num = LinkedList()
   num_4 = LinkedList()
   
   num.insert(3)
   num.insert(1)
   num_4.insert(6)
   num_4.insert(5)
   num_4.insert(4)
   num_4.insert(2)
  
   
   expected = str(linked_list_zip(num,num_4))
   actual = '{1} -> {2} -> {3} -> {4} -> {5} -> {6} ->  Null'
   assert actual == expected
# test if the second list is short 
def test_second_list_short():
   num = LinkedList()
   num_4 = LinkedList()

   num.insert(7)
   num.insert(3)
   num.insert(1)
   num_4.insert(6)
   num_4.insert(5)
   num_4.insert(4)
   num_4.insert(2)
  
   
   expected = str(linked_list_zip(num_4,num))
   actual = '{2} -> {1} -> {4} -> {3} -> {5} -> {7} -> {6} ->  Null'
   assert actual == expected

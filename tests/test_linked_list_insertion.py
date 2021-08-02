
import pytest

from data_structures_algorth.challenge_linked_list_insertion.linked_list_insertion import LinkedListInsertion

#Can successfully add a node to the end of the linked list
def test_adding_to_end():
    first_obj = LinkedListInsertion()
    first_obj.append(5)
    assert  first_obj.head.value == 5
   

#Can successfully add multiple nodes to the end of a linked list
def test_adding_to_end_multiple_values():
    first_obj = LinkedListInsertion()
    first_obj.append(5)
    first_obj.append(4)

    assert  first_obj.head.value == 5
    assert first_obj.head.next.value == 4

#Can successfully insert after a node in the linked list

def test_insert_after():
    second_obj = LinkedListInsertion()
    
    second_obj.append(1)
    second_obj.append(2)
    second_obj.append(3)
    second_obj.append(5)
    second_obj.add_after(3,6)

    expected = str(second_obj)
    actual = '{1} -> {2} -> {3} -> {6} -> {5} ->  Null'
    assert actual == expected

# if the value was not exist will return same 
def test_insert_after_with_unexisted_value():
    second_obj = LinkedListInsertion()
    
    second_obj.append(1)
    second_obj.append(2)
    second_obj.append(3)
    second_obj.append(5)
    second_obj.add_after(7,6)

    expected = str(second_obj)
    actual = '{1} -> {2} -> {3} -> {5} ->  Null'
    assert actual == expected
# if the value was not exist will return same 
def test_insert_before_with_unexisted_value():
    second_obj = LinkedListInsertion()
    
    second_obj.append(1)
    second_obj.append(2)
    second_obj.append(3)
    second_obj.append(5)
    second_obj.add_before(7,6)

    expected = str(second_obj)
    actual = '{1} -> {2} -> {3} -> {5} ->  Null'
    assert actual == expected

# Can successfully insert a node before the first node of a linked list 
def test_insert_after_with_unexisted_value():
    new_obj = LinkedListInsertion()
    
    new_obj.add_before(1,2)
    

    expected = str(new_obj)
    actual = '{2} -> {1} ->  Null'
    assert actual == expected

#Can successfully insert a node before the node of a linked list
def test_insert_before():
    third_obj = LinkedListInsertion()
    third_obj.append(1)
    third_obj.append(2)
   
    third_obj.add_before(2,6)

    expected = str(third_obj)
    actual = '{1} -> {6} -> {2} ->  Null'

    assert actual == expected

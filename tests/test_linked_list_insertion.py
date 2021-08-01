
import pytest

from data_structures_algorth.challenge_linked_list_insertion.linked_list_insertion import LinkedListInsertion

#Can successfully add a node to the end of the linked list
def test_adding_to_end():
    first_obj = LinkedListInsertion()
    first_obj.append(5)
    
    expected = str(first_obj)
    actual = "{5} ->  Null"
    assert actual == expected

#Can successfully add multiple nodes to the end of a linked list
def test_adding_to_end():
    first_obj = LinkedListInsertion()
    first_obj.append(5)
    first_obj.append(3)
    first_obj.append(7)
    
    expected = str(first_obj)
    actual = '{5} -> {3} -> {7} ->  Null'
    assert actual == expected
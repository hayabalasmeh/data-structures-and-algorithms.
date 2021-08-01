
import pytest

from data_structures_algorth.linked_list import LinkedList,Node

#test creation of node
def test_create_node():
       assert Node()

# test Node is contructed with data and it is assigned to the attribute "value"
def test_node_constructed_with_data():
       first_node = Node('Hi_1')
       expected = 'Hi_1'
       actual = first_node.value
       assert actual == expected

def test_node_next():
       second_node = Node('Hi_2')
       actual = second_node.next   
       assert True

def test_linked_list_class_instant():
       assert LinkedList()

def test_lined_list_head():
        third_list = LinkedList()
        actual = third_list.head
        assert True
  
def test_linked_list_insert():
       new_list = LinkedList()

       with pytest.raises(AttributeError):
              new_list.head.value
       expected = 1
       new_list.insert(1)
       actual = new_list.head.value
       
       assert actual == expected

def test_linked_list_multiple_insert():
       other_list = LinkedList()
       with pytest.raises(AttributeError):
              other_list.head.value
              #ignore the error of head value of none
       other_list.insert(1)
       other_list.insert(2)
       expected = 2
       actual = other_list.head.value
       
       assert actual == expected

#check if Will return true when finding a value within the linked list that exists
def test__finding_existed_value():
       expected = True
       integers_list = LinkedList()
       integers_list.insert(1)
       integers_list.insert(2)
       integers_list.insert(3)
       actual = integers_list.includes(2)
       assert expected == actual

#check Will return false when searching for a value in the linked list that does not exist
def test__finding_nonexisted_value():
       expected = False
       integers_list = LinkedList()
       integers_list.insert(1)
       integers_list.insert(2)
       integers_list.insert(3)
       actual = integers_list.includes(7)
       assert expected == actual
# check if Can properly return a collection of all the values that exist in the linked list
def test_showing_collection():
       expected = "{3} -> {2} -> {1} ->  Null"
       integers_list = LinkedList()
       integers_list.insert(1)
       integers_list.insert(2)
       integers_list.insert(3)
       actual = str(integers_list)
       assert expected == actual

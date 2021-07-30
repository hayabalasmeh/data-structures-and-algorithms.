
import pytest

from data_structures_algorth.linked_list import Linked_list,Node

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
       assert Linked_list()

def test_lined_list_head():
        other_list = Linked_list()
        actual = other_list.head
        assert True
  
def test_linked_list_insert():
       new_list = Linked_list()

       with pytest.raises(AttributeError):
              new_list.head.value
       expected = 1
       new_list.insert(1)
       actual = new_list.head
       
       assert actual == expected

def test_linked_list_multiple_insert():
       other_list = Linked_list()
       with pytest.raises(AttributeError):
              other_list.head.value
              #ignore the error of head value of none
       other_list.insert(1)
       other_list.insert(2)
       expected = 2
       actual = other_list.head
       
       assert actual == expected
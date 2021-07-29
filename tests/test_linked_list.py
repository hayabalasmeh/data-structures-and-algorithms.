
import pytest

from data_structures_algorth.linked_list import Linked_list

def test_linked_list_class_instant():
       assert Linked_list()
  
def test_linked_list_insert():
       test = Linked_list()

       with pytest.raises(AttributeError):
              test.head.value

       test.insert('Hi')
       actual = test.head.value
       expected = 'Hi'
       assert actual == expected
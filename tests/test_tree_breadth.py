
import pytest

from data_structures_algorth.challenge_tree_breadth.tree_breadth import tree_breadth_traverse
from data_structures_algorth.challenge_tree.tree import BinaryTree,Node

# Check if it raises an exception in case of empty tree

def test_empty_tree_breradth():

    #Arrange
    empty_tree = BinaryTree()

    #Act

    with pytest.raises(Exception) as excinfo:

         tree_breadth_traverse(empty_tree)

    # Assert
    assert 'The tree is empty' == str(excinfo.value)

# Check the happy path that the order of the nodes in the list is as expected

def test_breadth_traverse():
    #Arrange
    test_tree = BinaryTree()
    
    test_tree.root = Node(2)
    test_tree.root.left = Node(7)
    test_tree.root.right = Node(5)
    test_tree.root.right.right = Node(9)
    test_tree.root.right.right.left = Node(4)
    test_tree.root.left.left= Node(2)
    test_tree.root.left.right= Node(6)
    test_tree.root.left.right.right= Node(11)
    test_tree.root.left.right.left= Node(5)

    #Act
    actual =tree_breadth_traverse(test_tree)
    expected = [2,7,5,2,6,9,5,11,4]

    #Assert 
    assert actual == expected


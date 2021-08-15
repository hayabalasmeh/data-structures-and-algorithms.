
import pytest

from data_structures_algorth.challenge_tree.tree import BinaryTree,Node

# Check if it returns none in case of empty tree

def test_empty_tree():
    #Arrange
    binary_tree = BinaryTree()

    #Act
    actual = binary_tree.max_value(binary_tree.root)
    expected = None

    #Assert
    assert actual == expected


# Check if it raises an exception in case of comparing non numeric type of values

def test_nonnumeric_tree():
    #Arrange
    binary_tree = BinaryTree()
    binary_tree.root = Node(5)
    binary_tree.root.right = Node('A')
    binary_tree.root.left = Node(7)

    #Act
    with pytest.raises(Exception) as excinfo:
         binary_tree.max_value(binary_tree.root)
    

    #Assert
    assert 'We cannot compare non numeric type of data' == str(excinfo.value)

# Check if it return the maximum value of the nodes in a tree , happy path

def test_max_value_tree():
    #Arrange
    binary_tree_one = BinaryTree()
    binary_tree_one.root = Node(5)
    binary_tree_one.root.right = Node(8)
    binary_tree_one.root.left = Node(7)
    binary_tree_one.root.left.left = Node(4)
    binary_tree_one.root.left.right = Node(9)

    #Act
    actual = binary_tree_one.max_value(binary_tree_one.root)
    expected = 9
    

    #Assert
    assert actual == expected


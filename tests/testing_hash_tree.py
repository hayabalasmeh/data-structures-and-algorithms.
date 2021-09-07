from data_structures_algorth.challenge_hashtable.hashtable import HashTable
from data_structures_algorth.challenge_tree_hash.tree_intersect_hash import find_common_val
from data_structures_algorth.challenge_tree.tree import BinaryTree,Node

#Can successfully return the first occurence of the word

def test_find_common():
    #Arrange
    first = BinaryTree()
    first.root = Node('5')
   
    first.root.right = Node('4')
    first.root.left = Node('7')
    second = BinaryTree()
   
    second.root = Node('5')
    second.root.right = Node('4')
    second.root.left = Node('1')
    second.root.left.left = Node('7')
   
    #Act
    common = find_common_val(first,second)

    #Assert
    assert common== [5,4,7]

#Can successfully return empty list if both trees are empty

def test_find_common_empty():
    #ARRange
    first = BinaryTree()
    second = BinaryTree()
    #Act
    common = find_common_val(first,second)

    #Assert
    assert common == []

#Can successfully return the first occurence of the word if it has extra character

def test_find_common_one_tree_empty():
     #Arrange
    first = BinaryTree()
    second = BinaryTree()
    second.root = Node(5)
    second.root.left = Node(7)
    #Act
    common = find_common_val(first,second)

    #Assert
    assert common == []

def test_find_common_no_match():
     #Arrange
    first = BinaryTree()
    first.root = Node('5')
   
    first.root.right = Node('4')
    first.root.left = Node('7')
    second = BinaryTree()
   
    second.root = Node('8')
    second.root.right = Node('41')
    second.root.left = Node('1')
    second.root.left.left = Node('9')
   
    #Act
    common = find_common_val(first,second)

    #Assert
    assert common== []




import pytest

from data_structures_algorth.challenge_tree.tree import BinarySearch,BinaryTree, Node

#Can successfully instantiate an empty tree

def test_empty_tree():
    binary_tree = BinaryTree()
    assert binary_tree


# Can successfully instantiate a tree with a single root node


def test_root_tree():
    binary_tree = BinaryTree()
    binary_tree.root = Node('A')
    assert binary_tree.root.value == "A"


# Can successfully add a left child and right child to a single root node
def test_left_right_tree():
    binary_tree = BinaryTree()
    binary_tree.root = Node('A')
    binary_tree.root.left = Node('B')
    binary_tree.root.right = Node('C')
    assert binary_tree.root.left.value == "B" and binary_tree.root.right.value == 'C'


# Can successfully return a collection from a preorder traversal
def test_preorder_tree():
    binary_tree = BinaryTree()
    binary_tree.root = Node('A')
    binary_tree.root.left = Node('B')
    binary_tree.root.right = Node('C')
    binary_tree.root.right.left = Node('F')
    binary_tree.root.left.left = Node('D')
    binary_tree.root.left.right = Node('E')
    assert binary_tree.pre_order(binary_tree.root) == ['A','B','D','E','C','F']


# Can successfully return a collection from an inorder traversal
def test_inorder_tree():
    binary = BinaryTree()
    binary.root = Node('A')
    binary.root.left = Node('B')
    binary.root.right = Node('C')
    binary.root.right.left = Node('F')
    binary.root.left.left = Node('D')
    binary.root.left.right = Node('E')
    assert binary.in_order(binary.root) ==  ['D', 'B', 'E', 'A', 'F', 'C']
   


# Can successfully return a collection from a postorder traversal

def test_postorder_tree():
    binary = BinaryTree()
    binary.root = Node('A')
    binary.root.left = Node('B')
    binary.root.right = Node('C')
    binary.root.right.left = Node('F')
    binary.root.left.left = Node('D')
    binary.root.left.right = Node('E')
    assert binary.post_order(binary.root) ==  ['D', 'E', 'B', 'F', 'C', 'A']

# can successfully add multiple values in order to binary search tree:
def test_binary_search_add():

    bt = BinarySearch()
    
    bt.add(10)
    bt.add(5)
    bt.add(55)
    bt.add(20)
    bt.add(2)
    bt.add(21)
    assert  bt.root.right.left.value == 20 and  bt.root.left.left.value == 2

# can successfully check if a value contained in a binary search tree:
def test_binary_search_contain():

    bt = BinarySearch()
    
    bt.add(10)
    bt.add(5)
    bt.add(55)
    bt.add(20)

    assert bt.contain(55) == True and bt.contain(34) == False


    
@pytest.fixture(autouse=True)
def clean():
  BinaryTree.nodes = []

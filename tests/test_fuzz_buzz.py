
from data_structures_algorth.challenge_fuzz_tree.fuzz_buzz_tree import tree_fizz_buzz,Node,KaryTree

# Check if it returns none in case of empty tree

def test_empty_tree():
    #Arrange
    k_tree = KaryTree()

    #Act
    actual = k_tree.root
    expected = None

    #Assert
    assert actual == expected

# Check the happy path

def test_kary_tree():
    #Arrange
    tree = KaryTree()
    tree.root = Node(3)
    tree.root.children_pointers.append(Node(5))
    tree.root.children_pointers.append(Node(15))
    
    #Act
    actual = tree_fizz_buzz(tree.root)
    
    #Assert
    assert tree.root.value == 'Fizz' and tree.root.children_pointers[0].value == "Buzz" and tree.root.children_pointers[1].value == 'FizzBuzz'

# Check if it return the string value of the number in case the value was numbers other than 3,5,15

def test_other_numbers():
    #Arrange
    tree = KaryTree()
    tree.root = Node(3)
    tree.root.children_pointers.append(Node(7))
    tree.root.children_pointers.append(Node(15))
    
    #Act
    actual = tree_fizz_buzz(tree.root)
    
    #Assert
    assert tree.root.children_pointers[0].value == "7" 


from data_structures_algorth.challenge_stack_and_queue.stack_queue import Queue

# from data_structures_algorth.challenge_fuzz_tree.fuzz_buzz_tree

class Node:

   
    def __init__(self,value):
        """
        construct an object node with a value and a list of pointers to the children nodes

        """
       
        self.value = value
        self.children_pointers = []

class KaryTree:

     def __init__(self):
        """
        Construct K-ary tree object with a pointer to the root node of the tree
        """
        self.root = None



def tree_fizz_buzz(root):
    if root == None:
        return root
    traverser = Queue()
    traverser.enqueue(root)
    if root.value % 15 == 0:
           root.value = 'FizzBuzz'
    if root.value % 5 == 0:
           root.value = 'Buzz'
    elif root.value % 3 == 0:
           root.value = 'Fizz'
    
    else:
           root.value = str(root.value)

    while traverser.front:
        front_node = traverser.dequeue()
      

        for child in front_node.children_pointers:
            if child.value % 15 == 0:
               child.value = 'FizzBuzz'
            elif child.value % 5 == 0:
               child.value = 'Buzz'
            elif child.value % 3 == 0:
               child.value = 'Fizz'
            
            else:
               child.value = str(child.value)
            traverser.enqueue(child)
    return root

if __name__=='__main__':
    tree = KaryTree()
    tree.root = Node(3)
    tree.root.children_pointers.append(Node(5))
    tree.root.children_pointers.append(Node(15))
    print(tree.root.children_pointers[0].value)
    print(tree.root.children_pointers[1].value)
    print(tree_fizz_buzz(tree.root))
    print(tree.root.value)
    print(tree.root.children_pointers[0].value)
    print(tree.root.children_pointers[1].value)


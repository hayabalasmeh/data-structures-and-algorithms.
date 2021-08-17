from data_structures_algorth.challenge_stack_and_queue.stack_queue   import Queue
from data_structures_algorth.challenge_tree.tree import BinaryTree, Node
# from data_structures_algorth.challenge_tree_breadth.tree_breadth

def tree_breadth_traverse(tree):
    if tree.root == None:
        raise Exception('The tree is empty')

    tree_nodes = [] # to add the tree nodes to the list
    traverser = Queue() #will traverse using queue data structure
    traverser.enqueue(tree.root) #will start the traverse from the root node of the tree

    while traverser.front:
        front_node = traverser.dequeue()# to return the front node which added the first time 
        tree_nodes.append(front_node.value)

        if front_node.left:
            traverser.enqueue(front_node.left)
        
        if front_node.right:
            traverser.enqueue(front_node.right)
    return tree_nodes

if __name__ =='__main__':
    test_tree = BinaryTree()
    # print(tree_breadth_traverse(test_tree))
    test_tree.root = Node(2)
    test_tree.root.left = Node(7)
    test_tree.root.right = Node(5)
    test_tree.root.right.right = Node(9)
    test_tree.root.right.right.left = Node(4)
    test_tree.root.left.left= Node(2)
    test_tree.root.left.right= Node(6)
    test_tree.root.left.right.right= Node(11)
    test_tree.root.left.right.left= Node(5)
    print(tree_breadth_traverse(test_tree))


# from data_structures_algorth.challenge_tree.tree 
## creation of my class node 
from data_structures_algorth.challenge_stack_and_queue.stack_queue import Queue

class Node:

   
    def __init__(self,value):
        """
        construct an object node with a value and a pointer to the next node
        """
        self.right = None
        self.left = None 
        self.value = value
        

## creation of my Binary tree class
class BinaryTree:
    
    nodes = [] #To add all the nodes

    def __init__(self):
        """
        Construct Binary tree object with a pointer to the root node of the tree
        """
        self.root = None
        self.max = self.root
    
    def pre_order(self,root):
        """
        Traverse through the tree and return the values of the node in an order of root---left--right
        """

        self.nodes.append(root.value)

        if root.left:
            self.pre_order(root.left)

        if root.right:
            self.pre_order(root.right)

        return self.nodes

    def in_order(self,root):
        """
        Traverse through the tree and return the values of the node in an order of left--root--right
        """

        if root.left:
            self.in_order(root.left)

        self.nodes.append(root.value)

        if root.right:
            self.in_order(root.right)

        return self.nodes
    
    def post_order(self,root):
        """
        Traverse through the tree and return the values of the node in an order of left---right-root
        """
       
        if root.left:
            self.post_order(root.left)

        if root.right:
            self.post_order(root.right)

        self.nodes.append(root.value)

        return self.nodes

    def max_value(self,root):
        """
        Compare the values of the nodes and return the maximum value
        """
        if root == None: #Addressing the edge case of empty tree
            return None 

        if type(root.value) == str: #Addressing non numeric type of data
            raise Exception('We cannot compare non numeric type of data')

        if self.max == None:
            self.max = self.root.value
        
        if root.value > self.max: # with each traversal compare the value of the node with the max prop
            self.max = root.value

        if root.left:
            self.max_value(root.left)
        
        if root.right:
            self.max_value(root.right)

        return self.max #returning the max value after completing all the calls and compare it with all of the nodes
    def max_value_other_way(self):
        if self.root == None: #Addressing the edge case of empty tree
            return None 

        if type(self.root.value) == str: #Addressing non numeric type of data
            raise Exception('We cannot compare non numeric type of data')
        max = self.root.value
        self.pre_order(self.root)
        for item in self.nodes:
            if item > max:
                max = item
        return max
        
    def max_value_queue_way(self):
        checker = Queue()
        checker.enqueue(self.root)
        max = self.root.value

        while checker.front:
            node = checker.dequeue() # will dequeue the front node
            if node.value > max:
                max = node.value
            if node.left:
                checker.enqueue(node.left)
            if node.left:
                checker.enqueue(node.right)
        return max


    

## creation of Binary search class
class BinarySearch(BinaryTree):

    def add(self,value):
        """
        Add a value according to either right if it was greater than the root node or left if it was smaller than the root node 

        """
        node = Node(value)
        #check if the root is not empty
        if self.root == None:
            self.root = node
            return
        current = self.root
        
        while current: # 10 --- 20
            if current.value > value: 
               
                if current.left:
                   current= current.left
                   
                else:
                    current.left = node
                    return

            if current.value < value:

                if current.right:
                   current = current.right
                else:
                    current.right = node
                    return
           

       
    def contain(self,value):
        """
        Return True if a value is existed in the tree and return false if it's not
        """
        if value == self.root :
            return True

        current = self.root
        
        while current:
            if current.value > value: 
                if current.left:#10>5
                   current= current.left
                else:
                    return False
            if current.value < value:
                if current.right:
                   current = current.right 
                else:
                    return False

            if current.value == value:
                return True  
        return False


if __name__=="__main__":
    binary_tree = BinaryTree()
    binary_tree.root = Node('A')
    binary_tree.root.left = Node('B')
    binary_tree.root.right = Node('C')
    binary_tree.root.right.left = Node('F')
    binary_tree.root.left.left = Node('D')
    binary_tree.root.left.right = Node('E')

    by = BinaryTree()
    by.root = Node(2)
    by.root.right = Node(5)
    by.root.left = Node(7)
    by.root.left.left= Node(2)
    by.root.left.right= Node(6)
    by.root.left.right.right= Node(11)
    by.root.left.right.left= Node(5)
    by.root.right.right = Node(9)
    by.root.right.right.left = Node(4)
    print(by.max_value_queue_way())
    byyy = BinaryTree()
    byyy.root = Node(-2)
    byyy.root.right = Node(-5)
    byyy.root.left = Node(-7)
    print(byyy.max_value(byyy.root))
    byy = BinaryTree()
    byy.root = Node(2)
    byy.root.right = Node(5)
    byy.max_value(byy.root)
    # print(byy.max)
    # print(binary_tree.max_value(binary_tree.root))
    # print(binary_tree.in_order(binary_tree.root))

    bt = BinarySearch()
    
    bt.add(10)
    bt.add(5)
    bt.add(55)
    bt.add(20)
    bt.add(2)
    bt.add(21)
   
    # print(bt.contain(10))
    # print(bt.contain(0))
    # print(bt.root.left.value)
    # print(bt.root.right.value)
    # print(bt.root.right.left.value)
    # print(bt.root.left.left.value)
    # print(bt.contain(5))
    # print(bt.contain(55))
    # print(bt.contain(20))
    # print(bt.contain(27))
    # print(bt.contain(28))
    # print(binary_tree.post_order(binary_tree.root))
    # print(binary_tree.post_order(binary_tree.root))





    
    
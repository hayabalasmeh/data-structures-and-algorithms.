
# from data_structures_algorth.challenge_tree.tree 
## creation of my class node 

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
    
    nodes = []
    def __init__(self):
        """
        construct Binary tree object with a pointer to the root node of the tree
        """
        self.root = None
    
    def pre_order(self,root):

        self.nodes.append(root.value)

        if root.left:
            self.pre_order(root.left)

        if root.right:
            self.pre_order(root.right)

        return self.nodes

    def in_order(self,root):

        if root.left:
            self.in_order(root.left)

        self.nodes.append(root.value)

        if root.right:
            self.in_order(root.right)

        return self.nodes
    
    def post_order(self,root):
       
        if root.left:
            self.post_order(root.left)

        if root.right:
            self.post_order(root.right)

        self.nodes.append(root.value)

        return self.nodes


## creation of Binary search class
class BinarySearch(BinaryTree):

    def add(self,value):
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
    # print(binary_tree.in_order(binary_tree.root))

    bt = BinarySearch()
    
    bt.add(10)
    bt.add(5)
    bt.add(55)
    bt.add(20)
    bt.add(2)
    bt.add(21)
   
    print(bt.contain(10))
    print(bt.contain(0))
    print(bt.root.left.value)
    print(bt.root.right.value)
    print(bt.root.right.left.value)
    print(bt.root.left.left.value)
    print(bt.contain(5))
    print(bt.contain(55))
    print(bt.contain(20))
    print(bt.contain(27))
    print(bt.contain(28))
    # print(binary_tree.post_order(binary_tree.root))
    print(binary_tree.post_order(binary_tree.root))





    
    
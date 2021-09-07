from data_structures_algorth.challenge_hashtable.hashtable import HashTable
from data_structures_algorth.challenge_tree.tree import BinaryTree, Node

def find_common_val(first_tree,second_tree):
        common_values = []
        if not first_tree.root and not second_tree.root:
            return common_values
        elif not first_tree.root and  second_tree.root:
            return common_values
        elif first_tree.root and not second_tree.root:
            return common_values
        hash_map = HashTable()
        traverse(first_tree.root, hash_map)
        find(second_tree.root,common_values,hash_map)

        return common_values

def traverse(root,hash):
    hash.add(root.value,0)
    if root.left:
        traverse(root.left,hash)
    if root.right:
        traverse(root.right,hash)
    return hash

def find(root,common_values,hash):
    if hash.contains(root.value):
        common_values.append(int(root.value))
    if root.left:
        find(root.left,common_values,hash)
    if root.right:
        find(root.right,common_values,hash)
    return common_values

if __name__=="__main__":
    
    first = BinaryTree()
    first.root = Node('5')
   
    first.root.right = Node('4')
    first.root.left = Node('7')
    second = BinaryTree()
   
    second.root = Node('5')
    second.root.right = Node('4')
    second.root.left = Node('1')
    second.root.left.left = Node('7')
    print(find_common_val(first,second))
    

class Node:
    
    # This class represents a node in a binary tree
    # Each node represents one element in a binary tree with a value
    def __init__(self, value, left = None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    # Shows how the node is displayed when the memory is printed
    # Returns a string like Node(A), rather than a memory address
    def __str__(self):
        return "Node(" + str(self.value) + ")"

def walk(tree):
    
    if tree is not None:
        # print(tree)
        walk(tree.left)
        # print(tree)
        walk(tree.right)
        print(tree)

def walk2(tree, stack):
    
    # This is appending just the root Node of the binary tree
    stack.append(tree)
    
    while len(stack) > 0: 
        
        node = stack.pop()
         
        if node is not None:
            print(node)
            
            # Order right, left because we are in a stack FILO
            stack.append(node.right)
            stack.append(node.left)
        
# We are going to create an instance of the Node class

mytree = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G')))

walk(mytree)

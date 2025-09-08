# This is another way to traverse the tree, iterative method

def walk2(tree, stack):
    
    # Initiate the stack with the root node of the tree
    stack.append(tree)
    
    # While loop to iterate until stack is 0
    while(len(stack) > 0):
        
        # pop.() -> removes and returns the most recently added element (top of stack)
        node = stack.pop()
        
        # Checking to see if the top element has a value
        if node is not None:
            print(node)
            stack.append(node.right)
            stack.append(node.left)        
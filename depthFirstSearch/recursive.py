# Defining a function called walk using a pre-order dfs
def walk(tree):

    if tree is not None:
        print(tree) # Pre-order
        walk(tree.left)
        walk(tree.right)
        
    # if tree is not None:
    #     walk(tree.left)
    #     print(tree) -> In-order
    #     walk(tree.right)
    
    # if tree is not None:
    #     walk(tree.left)
    #     walk(tree.right)
    #     print(tree) -> Post-order
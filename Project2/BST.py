# Class for Binary Search Tree, inherits all methods from Tree class
# Contains Node class and method for insert

from Tree import Tree

class BST(Tree):
    # Node class contains its key, parent node, left child node, and right child node
    class Node:
        def __init__ (self, key):
            self.key = key
            self.parent = None
            self.left = None
            self.right = None

    # BST is created with no root and a size of zero
    def __init__(self):
        super().__init__()

    # Insert a new node with value key at position node 
    def insert(self, node, key):
        # If first node in tree
        if self.size == 0:
            self.root = self.Node(key)
            self.size += 1
            return self.root

        parent = None
        
        # Find position of new node
        while node is not None:
            parent = node
            if key < node.key:
                node = node.left
            else:
                node = node.right
        
        node = self.Node(key)
        node.parent = parent

        if node.key < parent.key:
            parent.left = node

        else:
            parent.right = node
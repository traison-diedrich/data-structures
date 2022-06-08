# Class for Red-Black Tree, inherits all methods from Tree class
# Contains Node class and methods for insert, insert fixup, right rotation, left rotation, print color, print parent color, and print uncle color

from Tree import Tree

class RBT(Tree):
    # Node class contains its key, parent node, left child node, right child node, and color
    class Node:
        def __init__(self, key, color = "R"):
            self.key = key
            self.left = None
            self.right = None
            self.parent = None
            self.color = color

    def __init__(self):
        super().__init__()

    # Insert a new node with value key at position node
    def insert(self, node, key):
        # If first node in tree
        if self.size == 0:
            self.root = self.Node(key, 'B')
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
        
        node = self.Node(key, 'R')
        node.parent = parent

        if node.key < parent.key:
            parent.left = node

        else:
            parent.right = node

        self.insertFixup(node)

    # Implement RBT insert-fixup procedure at position node
    def insertFixup(self, node):
        while node.parent and node.parent.color == "R":
            if node.parent.parent.left and node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y and y.color == 'R':
                    node.parent.color = 'B'
                    y.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                elif node.parent.right and node == node.parent.right:
                    node = node.parent
                    self.rotateLeft(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.rotateRight(node.parent.parent)
                elif node.parent.left and node == node.parent.left:
                    node = node.parent
                    self.rotateRight(node)
            elif node.parent.parent.right and node.parent == node.parent.parent.right:
                y = node.parent.parent.left
                if y and y.color == 'R':
                    node.parent.color = 'B'
                    y.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                elif node.parent.left and node == node.parent.left:
                    node = node.parent
                    self.rotateRight(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.rotateLeft(node.parent.parent) 
                elif node.parent.right and node == node.parent.right:
                    node = node.parent
                    self.rotateLeft(node)
        self.root.color = 'B'

    # Rotate right at position node
    def rotateRight(self, node):
        y = node.left
        node.left = y.right
        if y.right:
            y.right.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    # Rotate left at position node
    def rotateLeft(self, node):
        y = node.right
        node.right = y.left
        if y.left:
            y.left.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    # Print the color of key if key is found in tree
    def printColor(self, key):
        ans = self.search(self.root, key)
        if ans is None:
            return
        else:
            print("The color of", ans.key, "is", ans.color)

    # Print the parent color if key is found in tree
    def printParentColor(self, key):
        ans = self.search(self.root, key)
        if ans is None:
            return
        if ans.parent is None:
            print("The parent of", ans.key, "is NIL")
        else:
            print("The parent color of", ans.key, "is", ans.parent.color)

    # Print the Uncle color if key is found in tree
    def printUncleColor(self, key):
        ans = self.search(self.root, key)
        if ans is None:
            return
        if ans.parent is None:
            print("The parent of", ans.key, "is NIL")
        grandparent = ans.parent.parent
        if grandparent is None:
            print("The grandparent of", ans.key, "is NIL")
        if ans.parent == grandparent.left and grandparent.right:
            print("The Uncle color of", ans.key, "is", grandparent.right.color)
        if ans.parent == grandparent.left and not grandparent.right:
            print("The Uncle of", ans.key, "is NIL")
        if ans.parent == grandparent.right and grandparent.left:
            print("The Uncle color of", ans.key, "is", grandparent.left.color)
        if ans.parent == grandparent.right and not grandparent.left:
            print("The Uncle of", ans.key, "is NIL")




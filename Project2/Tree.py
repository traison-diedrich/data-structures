# Tree class for both Red-Black Tree and Binary Search Tree
# Contains methods for search, inorder traversal, print parent key, print left child, print right child, and print path to root

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    # Search for key starting at node
    def search(self, node, key):
        # Node could not be found
        if node is None:
            print("\nSorry,", str(key), "could not be found in the BST.")
            return node

        # Node was found
        if node.key == key:
            print("\nCongratulations!", str(key), "was found in the BST.")
            return node

        # Traverse right
        if node.key < key:
            return self.search(node.right, key)
            
        # Traverse left
        return self.search(node.left, key)

    # Inorder traversal starting at root and writing to file for every element in tree
    def inOrder(self, root, file):
        if root:
            self.inOrder(root.left, file) 
            file.write(str(root.key) + '\n')
            self.inOrder(root.right, file)

    # Prints the parent key if key is found in tree
    def printParentKey(self, key):
        ans = self.search(self.root, key)
        if ans is None:
            return
        if ans.parent is None:
            print("The parent is NIL")
        else:
            print("The parent of", key, "is", ans.parent.key)
        return ans

    # Prints left child if key is found in tree
    def printLeftChild(self, key):
        ans = self.search(self.root, key)
        if ans is None:
            return
        if ans.left is None:
            print("The left child is NIL")
        else:
            print("The left child of", key, "is", ans.left.key)

    # Prints right child if key is found in tree
    def printRightChild(self, key):
        ans = self.search(self.root, key)
        if ans is None:
            return
        if ans.right is None:
            print("The right child is NIL")
        else:
            print("The right child of", key, "is", ans.right.key)

    # Prints the path to the root, starting at the key (if found) and ending at NIL
    # Intial call must have node = None
    def printPathToRoot(self, node, key):
        if node is None:                            # base case
            node = self.search(self.root, key)
            if node is None:                        # making sure that key is found after searching
                return
        print(key, "-> ", end = "")
        if node.parent:
            self.printPathToRoot(node.parent, node.parent.key)
        else:
            print("NIL")
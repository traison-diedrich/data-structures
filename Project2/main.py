import time
from BST import BST
from RBT import RBT

# ######################## #
# Initial UI               #
# ######################## #

# Allows user to select the file type for input
def selectFileType():
    x = 9
    while (x !=0):
        print('\nEnter which type of file you wish to use.')
        print('1: Unsorted Data')
        print('2: Sorted Data')
        print('0: Exit')
        try:
            x = int(input('Choice: '))
            if x == 0:
                raise SystemExit
            elif x == 1:
                selectFile(1)
            elif x == 2:
                selectFile(2)
            else:
                print("\nThat number was not an option. Please try again.\n")
        except ValueError:
            print("\nThat was not a valid number. Please try again.\n")

# Arrays for selecting the file from a file type
unsorted = ['perm15K.txt', 'perm30K.txt','perm45K.txt','perm60K.txt','perm75K.txt','perm90K.txt','perm105K.txt','perm120K.txt','perm135K.txt','perm150K.txt']
sorted = ['sorted15K.txt', 'sorted30K.txt', 'sorted45K.txt', 'sorted60K.txt', 'sorted75K.txt', 'sorted90K.txt', 'sorted105K.txt', 'sorted120K.txt', 'sorted135K.txt', 'sorted150K.txt']
arr = [unsorted, sorted]

# Allows user to select an individual file from the indicated file type
def selectFile(fileType):
    x = 9
    while (x!=0):
        print('\nEnter which file you would like to use.')
        for x in range(len(arr[fileType-1])):
            print(str(x+1) + ': ' + str(arr[fileType-1][x]))
        print('0: Exit')
        try:
            x = int(input('Choice: '))
            if x == 0:
                raise SystemExit
            elif (x > 0 and x <= 10):
                selectTreeType(arr[fileType-1][x-1])
            else:
                print("\nThat number was not an option. Please try again.\n")
        except ValueError:
            print("That was not a valid number. Please try again.")

# Allows the user to select between constructin a BST or RBT
def selectTreeType(file):
    x = 9
    while (x!=0):
        print('\nEnter which type of tree you would like to build for', str(file) + '.')
        print('1: Binary Search Tree')
        print('2: Red-Black Tree')
        print('0: Exit')
        try:
            x = int(input('Choice: '))
            if x == 0:
                raise SystemExit
            elif x == 1:
                buildBST(file)
            elif x == 2:
                buildRBT(file)
            else:
                print("\nThat number was not an option. Please try again.\n")
        except ValueError:
            print("\nThat was not a valid number. Please try again.\n")

# Creates an array element for every line in file, returns array
def getCleanArray(file):
    arr = []
    fileName = "./wordlists/" + file
    with open(fileName, 'r') as text:
        for line in text:
            strippedLine = line.strip()
            arr.append(strippedLine)
    return arr

# ######################## #
# BST Testing              #
# ######################## #

# Builds a BST for file and outputs construction time
# Also outputs an inorder traversal of the BST to a new file called "BST + file"
def buildBST(file):
    arr = getCleanArray(file)

    tree = BST()

    startTime = time.time()

    for word in arr:
        tree.insert(tree.root, word)

    print('\nThe BST construction time for', file, 'took', round((time.time()-startTime),7), 'seconds to run.')

    with open("BST" + file, 'a') as text:
        tree.inOrder(tree.root, text)

    print("An InOrder Traversal has been output to BST" + file + "\n")

    searchBST(tree)

# Allows the user to search for a word in the constructed tree, outputting the time taken to find the word
def searchBST(tree):
    x = 9
    while (x !=0):
        print('Would you like to search for a word in your BST?')
        print('1: Yes')
        print('2: No (Continue to other options)')
        print('0: Exit')
        try:
            x = int(input('Choice: '))
            if x == 0:
                raise SystemExit
            elif x == 1:
                ans = str(input("\nEnter a word you would like to search for: ")).upper()
                startTime = time.time()
                tree.search(tree.root, ans)
                print("The search for", ans, "took", round((time.time()-startTime),10), 'seconds to run.\n')
                searchBST(tree)
            elif x == 2:
                testBST(tree)
            else:
                print("\nThat number was not an option. Please try again.\n")
        except ValueError:
            print("\nThat was not a valid number. Please try again.\n")

# Allows the user to test additional methods on the tree
def testBST(tree):
    x = 9
    while (x !=0):
        print('\nWhat would you like to test on your BST?')
        print('1: Print the Parent Key')
        print('2: Print the Left Child')
        print('3: Print the Right Child')
        print('4: Print the Path to Root')
        print('5: Start from the beginning with a new input.')
        print('0: Exit')
        try:
            x = int(input('Choice: '))
            if x == 0:
                raise SystemExit
            elif x == 1:
                ans = str(input("\nEnter a word whose parent key you would like to print: ")).upper()
                tree.printParentKey(ans)
                testBST(tree)
            elif x == 2:
                ans = str(input("\nEnter a word whose left child you would like to print: ")).upper()
                tree.printLeftChild(ans)
                testBST(tree)
            elif x == 3:
                ans = str(input("\nEnter a word whose right child you would like to print: ")).upper()
                tree.printRightChild(ans)
                testBST(tree)
            elif x == 4:
                ans = str(input("\nEnter a word whose path to the root you would like to print: ")).upper()
                tree.printPathToRoot(None, ans)
                testBST(tree)
            elif x == 5:
                selectFileType()
            else:
                print("\nThat number was not an option. Please try again.\n")
        except ValueError:
            print("\nThat was not a valid number. Please try again.\n")

# ######################## #
# BST Testing              #
# ######################## #

# Builds a RBT for file and outputs construction time
# Also outputs an inorder traversal of the RBT to a new file called "RBT + file"
def buildRBT(file):
    arr = getCleanArray(file)

    tree = RBT()

    startTime = time.time()

    for word in arr:
        tree.insert(tree.root, word)

    print('\nThe RBT construction time for', file, 'took', round((time.time()-startTime),7), 'seconds to run.')

    with open("RBT" + file, 'a') as text:
        tree.inOrder(tree.root, text)

    print("An InOrder Traversal has been output to RBT" + file + "\n")

    searchRBT(tree)

# Allows the user to search for a word in the constructed tree, outputting the time taken to find the word
def searchRBT(tree):
    x = 9
    while (x !=0):
        print('Would you like to search for a word in your RBT?')
        print('1: Yes')
        print('2: No (Continue to other options)')
        print('0: Exit')
        try:
            x = int(input('Choice: '))
            if x == 0:
                raise SystemExit
            elif x == 1:
                ans = str(input("\nEnter a word you would like to search for: ")).upper()
                startTime = time.time()
                tree.search(tree.root, ans)
                print("The search for", ans, "took", round((time.time()-startTime),10), 'seconds to run.\n')
                searchRBT(tree)
            elif x == 2:
                testRBT(tree)
            else:
                print("\nThat number was not an option. Please try again.\n")
        except ValueError:
            print("\nThat was not a valid number. Please try again.\n")

# Allows the user to test additional methods on the tree
def testRBT(tree):
    x = 9
    while (x !=0):
        print('\nWhat would you like to test on your RBT?')
        print('1: Print the Color')
        print('2: Print the Parent Key')
        print('3: Print the Parent Color')
        print('4: Print the Left Child')
        print('5: Print the Right Child')
        print('6: Print the Uncle Color')
        print('7: Print the Path to Root')
        print('8: Start from the beginning with a new input.')
        print('0: Exit')
        try:
            x = int(input('Choice: '))
            if x == 0:
                raise SystemExit
            elif x == 1:
                ans = str(input("\nEnter a word whose color you would like to print: ")).upper()
                tree.printColor(ans)
                testRBT(tree)
            elif x == 2:
                ans = str(input("\nEnter a word whose parent key you would like to print: ")).upper()
                tree.printParentKey(ans)
                testRBT(tree)
            elif x == 3:
                ans = str(input("\nEnter a word whose parent color you would like to print: ")).upper()
                tree.printParentColor(ans)
                testRBT(tree)
            elif x == 4:
                ans = str(input("\nEnter a word whose left child you would like to print: ")).upper()
                tree.printLeftChild(ans)
                testRBT(tree)
            elif x == 5:
                ans = str(input("\nEnter a word whose right child you would like to print: ")).upper()
                tree.printRightChild(ans)
                testRBT(tree)
            elif x == 6:
                ans = str(input("\nEnter a word whose Uncle color you would like to print: ")).upper()
                tree.printUncleColor(ans)
                testRBT(tree)
            elif x == 7:
                ans = str(input("\nEnter a word whose path to the root you would like to print: ")).upper()
                tree.printPathToRoot(None, ans)
                testRBT(tree)
            elif x == 8:
                selectFileType()
            else:
                print("\nThat number was not an option. Please try again.\n")
        except ValueError:
            print("\nThat was not a valid number. Please try again.\n")

if __name__ == "__main__":
    selectFileType()
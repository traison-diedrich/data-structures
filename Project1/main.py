# ##################################### #
# Program to demonstrate the            #
#   complexity of 3 sorting algorithms  #
#                                       #
# Author: Traison Diedrich              #
# ##################################### #
from os import write
import time

""" 
The following three methods (selectSortType, selectFileType, and selectFile)
    are the UI for selecting which type of sorting algorithm to use and
    which file the sort will be performed on.
"""

def selectSortType():
    x = 9
    while (x!=0):
        print('Enter which type of sort you would like to execute.')
        print('1: Insertion Sort')
        print('2: Merge Sort')
        print('3: Heap Sort')
        print('0: Exit')
        try:
            x = int(input('Choice: '))
            if x == 0:
                raise SystemExit
            elif x == 1:
                selectFileType(1)
            elif x == 2:
                selectFileType(2)
            elif x == 3:
                selectFileType(3)
            else:
                print()
                print("That number was not an option. Please try again.")
                print()
        except ValueError:
            print()
            print("That was not a valid number. Please try again.")
            print()


def selectFileType(sortType):
    x = 9
    while (x !=0):
        print()
        print('Enter which type of files you wish to sort.')
        print('1: Unsorted Input')
        print('2: Sorted Input')
        print('0: Exit')
        try:
            x = int(input('Choice: '))
            if x == 0:
                raise SystemExit
            elif x == 1:
                selectFile(sortType, 0)
            elif x == 2:
                selectFile(sortType, 1)
            else:
                print()
                print("That number was not an option. Please try again.")
                print()
        except ValueError:
            print()
            print("That was not a valid number. Please try again.")
            print()

# arrays for selecting the file and file type
unsorted = ['perm15K.txt', 'perm30K.txt','perm45K.txt','perm60K.txt','perm75K.txt','perm90K.txt','perm105K.txt','perm120K.txt','perm135K.txt','perm150K.txt']
sorted = ['sorted15K.txt', 'sorted30K.txt', 'sorted45K.txt', 'sorted60K.txt', 'sorted75K.txt', 'sorted90K.txt', 'sorted105K.txt', 'sorted120K.txt', 'sorted135K.txt', 'sorted150K.txt']
arr = [unsorted, sorted]


def selectFile(sortType, fileType):
    x = 9
    while (x!=0):
        print()
        print('Enter which file you would like to run.')
        for x in range(len(arr[fileType])):
            print(str(x+1) + ': ' + str(arr[fileType][x]))
        print('11: All')
        print('0: Exit')
        try:
            x = int(input('Choice: '))
            if x == 0:
                raise SystemExit
            elif (x > 0 and x <= 10):
                sort(sortType, arr[fileType][x-1])
                selectSortType()
            elif (x == 11):
                for file in arr[fileType]:
                    sort(sortType, file)
                selectSortType()
            else:
                print()
                print("That number was not an option. Please try again.")
                print()
        except ValueError:
            print()
            print("That was not a valid number. Please try again.")
            print()

# method for inputting a file name as a string and converting it to an array
def getCleanArray(file):
    arr = []
    fileName = "./wordlists/" + file
    with open(fileName, 'r') as text:
        for line in text:
            strippedLine = line.strip()
            arr.append(strippedLine)
    return arr

# method for writing a sorted array to a text file
# 0 = Insertion Sort, 1 = Merge Sort, 2 = Heap Sort
def writeToTxt(arr, file, sortType):
    sorts = ['IS', 'MS', 'HS']
    fileEnd = ''
    for x in range(len(file)):
        if file[x].isnumeric() == True:
            fileEnd = file[x:]
            break
    
    with open(sorts[sortType] + fileEnd, 'w') as newText:
        for word in arr:
            newText.write(str(word) + '\n')
    

# method that runs insertion sort on the file, outputs the time for the sort, and writes the sorted array to a txt file
def insertionSort(file):
    arr = getCleanArray(file)

    startTime = time.time()

    # insertion sort start
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while i >=0 and arr[i] > key :
                arr[i+1] = arr[i]
                i -= 1
        arr[i+1] = key
    # insertion sort end
    
    print()
    print('The insertion sort for', file, 'took', round((time.time()-startTime),2), 'seconds to run.')
    print()

    writeToTxt(arr, file, 0)

# method for merging arrays used by merge sort
def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# merge sort method
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(arr, left, right)

# method that runs merge sort on the file, outputs time for the sort, and writes the sorted array to a txt file        
def mergeSortCombined(file):
    arr = getCleanArray(file)

    startTime = time.time()
    
    mergeSort(arr)

    print()
    print('The merge sort for', file, 'took', round((time.time()-startTime),2), 'seconds to run.')
    print()

    writeToTxt(arr, file, 1)

# method for max heapifying, used by heap sort
def heapify(arr, n, i):
    l = i*2+1
    r = i*2+2
    if (l < n and arr[l] > arr[i]):
        largest = l
    else:
        largest = i
    if (r < n and arr[r] > arr[largest]):
        largest = r
    if (largest != i):
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# method that runs heap sort on a file, outputs time for the sort, and writes the sorted array to a txt file
def heapSort(file):
    arr = getCleanArray(file)

    startTime = time.time()

    #Build Max Heap
    for i in range(len(arr)//2, -1, -1):
        heapify(arr, len(arr), i)

    #Swap and heapify root
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    #End of heap sort

    print()
    print('The heap sort for', file, 'took', round((time.time()-startTime),2), 'seconds to run.')
    print()

    writeToTxt(arr, file, 2)

# method which takes in a sort type and file, then calls the desired sorting algorithm
def sort(sortType, file):
    if sortType == 1:
        insertionSort(file)
    if sortType == 2:
        mergeSortCombined(file)
    if sortType == 3:
        heapSort(file)

if __name__ == '__main__':
    selectSortType()
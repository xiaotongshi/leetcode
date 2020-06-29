arr = [5,2,3,6,4,1,7]

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
# print(bubbleSort(arr))

#################################################
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minIndex = arr[i:].index(min(arr[i:]))
        arr[i], arr[i+minIndex] = arr[i+minIndex], arr[i]
    return arr
# print(selectionSort(arr))

#####################################################
def InsertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        preIndex = i-1
        curr = arr[i]
        while (preIndex >= 0) & (arr[preIndex] > curr):
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = curr
    return arr
# print(InsertionSort(arr))

##############################################
def shellSort(arr):
    n = len(arr)
    gap = int(n/2)
    while gap:
        for i in range(gap, n):
            j = i
            curr = arr[i]
            while (j-gap >= 0) & (arr[j-gap] > curr):
                arr[j] = arr[j-gap]
                j = j - gap
            arr[j] = curr
        gap = int(gap/2)
    return arr
print(shellSort(arr))

################################################
def mergeSort(arr):
    n = len(arr)
    if n < 2:
        return arr
    middle = int(n/2)
    left = arr[0:middle]
    right = arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    res = []
    while (len(left) > 0) & (len(right) > 0 ):
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    while len(left):
        res.append(left.pop(0))
    while len(right):
        res.append(right.pop(0))
    return res

# print(mergeSort(arr))

###########################################
def quickSort(arr, left, right):
    if left < right:
        partionIndex = partition(arr, left, right)
        quickSort(arr, left, partionIndex-1)
        quickSort(arr, partionIndex+1, right)
    return arr

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

# print(quickSort(arr, 0, len(arr)-1))

#############################################
def heapSort(arr):
    n = len(arr)
    # 开始时只需要扫描一半的元素（所有父节点），因为只有他们才有子节点 
    # 从最后一个父节点开始， 使父节点大于子节点的值
    for i in range(int(n/2)-1, -1, -1):
        adjust_heap(arr, i, n)

    # 将根节点（此时最大值）和最后一个子节点开始交换
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        adjust_heap(arr, 0, i)
    return arr

def adjust_heap(arr, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    parent = i
    # 如果左结点更大，和父节点交换
    if (left < n) & (arr[left] > arr[parent]):
        parent = left
    # 如果右结点更大，和父节点交换
    if (right < n) & (arr[right] > arr[parent]):
        parent = right
    if parent != i:
        arr[i], arr[parent] = arr[parent], arr[i]
        adjust_heap(arr, parent, n)

# print(heapSort(arr))
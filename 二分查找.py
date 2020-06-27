"""
1. 二分查找是有条件的，首先是有序，其次因为二分查找操作的是下标，所以要求是顺序表
2. 最优时间复杂度：O(1)
3. 最坏时间复杂度：O(logn)
"""

def binary_chop(alist, data):
    """
    递归解决二分查找
    :param alist:
    :return:
    """
    n = len(alist)
    if n < 1:
        return False
    mid = n // 2
    if alist[mid] > data:
        return binary_chop(alist[0:mid], data)
    elif alist[mid] < data:
        return binary_chop(alist[mid+1:], data)
    else:
        return True

def binary_chop2(alist, data):
    """
    非递归解决二分查找
    :param alist:
    :return:
    """
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (last + first) // 2
        if alist[mid] > data:
            last = mid - 1
        elif alist[mid] < data:
            first = mid + 1
        else:
            return True
    return False

if __name__ == '__main__':
    lis = [2,4, 5, 12, 14, 23]
    if binary_chop(lis, 14):
        print('ok')
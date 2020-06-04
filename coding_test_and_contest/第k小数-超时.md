https://ac.nowcoder.com/acm/contest/5773/A

# 题目描述 
给你一个长度为n的序列，求序列中第k小数的多少。

# 输入描述:
多组输入，第一行读入一个整数T表示有T组数据。
每组数据占两行，第一行为两个整数n，k，表示数列长度和k。
第二行为n个用空格隔开的整数。

# 输出描述:
对于每组数据，输出它的第k小数是多少。
每组数据之间用空格隔开

# 示例1
## 输入
2
5 2
1 4 2 3 4
3 3
3 2 1
## 输出
2
3

# 思路
快排，找到第k个就停止，不用全部排完

```python
import sys
# def partition(arr,low,high): 
#     i = low       
#     pivot = arr[high]   
#     for j in range(low , high): 
#         if  arr[j] <= pivot: 
#             arr[i], arr[j] = arr[j], arr[i]
#             i = i+1 
#     arr[i], arr[high] = arr[high], arr[i] 
#     return i

# def quickSort(arr,low,high, k): 
#     if low < high:
#         pi = partition(arr,low,high) 
#         if pi == k:
#             return arr
#         elif pi > k:
#             quickSort(arr,low, pi-1, k) 
#         else:
#             quickSort(arr,pi+1, high, k)
#     return arr

# n = int(input())
# for _ in range(n):
#     n, k = list(map(int, sys.stdin.readline().strip().split()))
#     x = list(map(int, sys.stdin.readline().strip().split()))
#     x = quickSort(x, 0, len(x)-1, k-1)
#     print(str(x[k-1]))

def quickSort(arr, k):
    if len(arr) < k:
        return arr
    tmp = arr[-1]
    left = [x for x in arr[:-1] if x <= tmp]
    nleft = len(left)
    if nleft == k-1:
        return tmp
    elif nleft > k-1:
        return quickSort(left, k)
    else:
        right = [x for x in arr[:-1] if x > tmp]
        return quickSort(right, k-(nleft+1))

n = int(input())
for _ in range(n):
    n, k = list(map(int, sys.stdin.readline().strip().split()))
    x = list(map(int, sys.stdin.readline().strip().split()))
    ans = quickSort(x, k)
    print(str(ans))
    # print(str(x[k-1]))
```

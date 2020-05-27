https://ac.nowcoder.com/acm/contest/5803/E

# 题目描述 
恬恬有一个nx n的数组。她在用这个数组玩游戏：
开始时，数组中每一个元素都是0。
恬恬会做某些操作。在一次操作中，她可以将某一行的所有元素同时加上一个值，也可以将某一列的所有元素同时加上一个值。
在几次操作后，一个元素被隐藏了。你能帮助她回忆隐藏的数是几吗？

# 输入描述
第一行一个整数n（1≤ n≤ 1000）。
接下来n行每行n个整数表示数组a。
第(i+1)行的第j个元素表示aij（aij=-1或0≤ aij ≤ 10000）。-1表示隐藏的元素。

# 输出描述
仅一个整数表示答案。

# 示例1
## 输入
3
1 2 1
0 -1 0
0 1 0
## 输出
1

# 思路
``data[i][cor_y] - data[i][i]``得到的是第在第i行cor_y列相对于第i列的差值
用同一行的``data[cor_x][i]`` 加上这个差值就是``data[cor_x][cor_y]``的真实值

```python
import sys
n = int(input())
data = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    data.append(temp)
    try:
        cor_y = temp.index(-1)
        cor_x = i
    except:
        pass

if cor_x == 0 or cor_y == 0:
    ans = data[cor_x][-1] + data[-1][cor_y] - data[-1][-1]
else:
    ans = data[cor_x][0] + data[0][cor_y] - data[0][0] 

print(str(ans))
```
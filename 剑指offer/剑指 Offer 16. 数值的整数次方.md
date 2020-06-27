https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/
# 题目描述
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

# 示例 1:
输入: 2.00000, 10
输出: 1024.00000

# 示例 2:
输入: 2.10000, 3
输出: 9.26100

# 示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25

# 思路：快速幂法，时间复杂度O(nlogn)
当n<0：x=1/x，n=-n
用二进制表达十进制正整数n，bm...b3b2b1   
x^n = x^(1b1+2b2+4b3+...+2^(m-1)bm) = x^(1b1)x^(2b2)x^(4b3)...x^(2^(m-1)bm)   
对于x^1, x^2...： 循环赋值操作 x = x^2   
对于二进制b1,b2,...bm的值：
1. n&1：判断当前二进制最右一位是否位1
2. n>>1：n向右移一位   


```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1/x
            n = -n
        ans = 1
        while n:
            if n & 1: 
                ans *= x
            x *= x # x^2
            n >>= 1 # 右移一位，更高位
        return ans
```
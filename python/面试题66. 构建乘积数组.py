class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        n = len(a)
        if n <2:
            return a
            
        b1 = [1] * n
        for i in range(n-2, -1, -1):
            b1[i] = b1[i+1] * a[i+1]
        b2 = [1] * n
        b = [1] * n
        b[0] = b1[0]
        for i in range(1, n):
            b2[i] = b2[i-1] * a[i-1]
            b[i] = b1[i] * b2[i]
        return b

a = [1,2,3,4,5]
print(Solution().constructArr(a))
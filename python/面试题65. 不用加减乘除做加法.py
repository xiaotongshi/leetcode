class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b: 
           a,b = (a^b) & 0xFFFFFFFF,((a&b)<<1) & 0xFFFFFFFF
        return a if a<=0x7FFFFFFF else ~(a^0xFFFFFFFF)

a = -1
b = 2
print(Solution().add(a,b))
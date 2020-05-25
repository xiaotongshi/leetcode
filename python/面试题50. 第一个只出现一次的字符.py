class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ' '
        d = dict() #无序字典，不按照输入的顺序
        for x in s:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        for x in s: # 按照输入的顺序查找
            if d[x]==1:
                return x
        return ' '


# s = "abaccdeff"
s = 'leetcode'
print(Solution().firstUniqChar(s))
class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        s = [str(x) for x in nums]
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if s[i]+s[j]>s[j]+s[i]:
                    s[i],s[j]=s[j],s[i]
        return "".join(s)


nums = [3,30,34,5,9]
print(Solution().minNumber(nums))
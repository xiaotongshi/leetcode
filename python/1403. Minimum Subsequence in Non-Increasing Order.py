class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = list(sorted(nums))
        ans = [s.pop()]
        while sum(ans) <= sum(s):
            ans.append(s.pop())
        return ans

nums = [4,3,10,9,8]
print(Solution().minSubsequence(nums))
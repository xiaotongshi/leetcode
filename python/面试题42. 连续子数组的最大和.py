class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = nums[0]
        for i in range(1,len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            maxnum = max(maxnum,nums[i])
        return maxnum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))
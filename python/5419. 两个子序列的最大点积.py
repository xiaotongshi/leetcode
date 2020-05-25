# 给你两个数组 nums1 和 nums2 。

# 请你返回 nums1 和 nums2 中两个长度相同的 非空 子序列的最大点积。

# 数组的非空子序列是通过删除原数组中某些元素（可能一个也不删除）后剩余数字组成的序列，但不能改变数字间相对顺序。比方说，[2,3,5] 是 [1,2,3,4,5] 的一个子序列而 [1,5,3] 不是。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/max-dot-product-of-two-subsequences
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m,n = len(nums1),len(nums2)
        INF = -100000000
        dp = [[INF]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = nums1[i-1] * nums2[j-1]
                dp[i][j] = max(dp[i-1][j], dp[i][j-1],  dp[i-1][j-1], 
                                dp[i-1][j-1] + nums1[i-1] * nums2[j-1])
        return dp[m][n]


nums1 = [2,1,-2,5]
nums2 = [3,0,-6]
print(Solution().maxDotProduct(nums1, nums2))
class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        # 遍历从2到n的长度
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i-j]*j, j*(i-j))
        return dp[n]
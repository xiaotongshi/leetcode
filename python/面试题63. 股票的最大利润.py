# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if len(prices) == 0:
#             return 0
#         ans = 0
#         cur = min(prices)
#         i = prices.index(cur)
#         while i>=0:
#             ans = max(ans, max(prices[i:]) - cur)
#             if i > 0:
#                 cur = min(prices[:i])
#                 i = prices.index(cur)
#             else:
#                 i = -1
#         return ans
class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        if length == 0:
            return 0
        cur_min = prices[0]  # 初始化最小的股票值，用来存储可以买入的最小值
        max_profit = 0  # 存储最终结果，即可以达到的最大利润
        for i in range(1, length):
            max_profit = max(max_profit, prices[i] - cur_min)  # 比较当前可以得到的最大利润和当前位置的利润
            cur_min = min(cur_min, prices[i])  # 更新目前的最小买入价格
        return max_profit


prices = [2,6,1,3]
print(Solution().maxProfit(prices))
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = cur = 0
        d = dict()
        for i in range(len(s)):
            j = d.get(s[i], -1)
            if i-j <= cur: # 说明在i到j之间没有出现过其他重复字符
                res = max(res, cur)
                cur = i-j
            else: # 说明在i到j之间已经出现过其他重复字符
                cur += 1
            d[s[i]] = i
        return max(res, cur)

print(Solution().lengthOfLongestSubstring("abcabcbb"))
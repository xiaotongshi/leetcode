# 给你一个字符串 s ，请你根据下面的算法重新构造字符串：

# 从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
# 从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。
# 重复步骤 2 ，直到你没法从 s 中选择字符。
# 从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
# 从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。
# 重复步骤 5 ，直到你没法从 s 中选择字符。
# 重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。
# 在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。

# 请你返回将 s 中字符重新排序后的 结果字符串 。

# Given a string s. You should re-order the string using the following algorithm:

# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

# Return the result string after sorting s with this algorithm.

import collections
class Solution:
    def sortString(self, s: str) -> str:
        str_counter = collections.Counter(s)
        result = []
        flag = False
        while str_counter:
            keys = list(str_counter.keys())
            keys.sort(reverse=flag)
            flag = not flag
            result.append(''.join(keys))
            str_counter -= collections.Counter(keys)
        return ''.join(result)

s =   "aaaabbbbcccc" # "abccbaabccba"
print(Solution().sortString(s))
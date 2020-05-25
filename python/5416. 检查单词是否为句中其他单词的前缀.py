# 给你一个字符串 sentence 作为句子并指定检索词为 searchWord ，其中句子由若干用 单个空格 分隔的单词组成。

# 请你检查检索词 searchWord 是否为句子 sentence 中任意单词的前缀。

# 如果 searchWord 是某一个单词的前缀，则返回句子 sentence 中该单词所对应的下标（下标从 1 开始）。
# 如果 searchWord 是多个单词的前缀，则返回匹配的第一个单词的下标（最小下标）。
# 如果 searchWord 不是任何单词的前缀，则返回 -1 。
# 字符串 S 的 「前缀」是 S 的任何前导连续子字符串。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        n = len(searchWord)
        sentence = sentence.split()
        for i, s in enumerate(sentence):
            try:
                if s[:n] == searchWord:
                    return i+1
            except:
                pass
        return -1

# sentence = "this problem is an easy problem"
# searchWord = "pro"
sentence = "hello from the other side"
searchWord = "they"
print(Solution().isPrefixOfWord(sentence, searchWord))
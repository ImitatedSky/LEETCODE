#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (32.85%)
# Likes:    2202
# Dislikes: 353
# Total Accepted:    571.8K
# Total Submissions: 1.7M
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string s and an array of strings words. All the strings of
# words are of the same length.
#
# A concatenated string is a string that exactly contains all the strings of
# any permutation of words concatenated.
#
#
# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef",
# "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is
# not a concatenated string because it is not the concatenation of any
# permutation of words.
#
#
# Return an array of the starting indices of all the concatenated substrings in
# s. You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
#
# Output: [0,9]
#
# Explanation:
#
# The substring starting at 0 is "barfoo". It is the concatenation of
# ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of
# ["foo","bar"] which is a permutation of words.
#
#
# Example 2:
#
#
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
#
# Output: []
#
# Explanation:
#
# There is no concatenated substring.
#
#
# Example 3:
#
#
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
#
# Output: [6,9,12]
#
# Explanation:
#
# The substring starting at 6 is "foobarthe". It is the concatenation of
# ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of
# ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of
# ["the","foo","bar"].
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.
#
#
#

# @lc code=start
# Time Limit Exceeded O(M*N)
# ex:s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa....." words = ["aaa", "aaa", "aaa"]
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         if not s or not words:
#             return []
#         n = len(words[0])
#         _len = len(words)*n

#         words_dict = {}
#         for i in words:
#             if i in words_dict:
#                 words_dict[i] +=1
#             else:
#                 words_dict[i] = 1
#         def check(d:dict,s,l):
#             d = d.copy()
#             for i in range(l):
#                 if s[i*n:(i+1)*n] in d:
#                     d[s[i*n:(i+1)*n] ] -=1
#                     if d[s[i*n:(i+1)*n] ] < 0:
#                         return False
#                 else:
#                     return False
#             return True
#         res = []
#         for i in range(0, len(s) - _len+1):
#             if check(words_dict,s[i:i+_len],len(words)):
#                 res.append(i)
#         return res


# from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_len * len(words)
        word_count = Counter(words)
        res = []

        for offset in range(word_len):  # 處理所有可能的偏移量
            left = right = offset
            window_count = Counter()
            count = 0  # 現在視窗內有幾個有效的 word

            while right + word_len <= len(s):
                word = s[right : right + word_len]
                right += word_len

                if word in word_count:
                    window_count[word] += 1
                    count += 1

                    # 若某個 word 超過預期次數，縮小視窗
                    while window_count[word] > word_count[word]:
                        left_word = s[left : left + word_len]
                        window_count[left_word] -= 1
                        count -= 1
                        left += word_len

                    # 若視窗內正好是所有 words 的總數，記錄結果
                    if count == len(words):
                        res.append(left)

                else:
                    # 清空視窗
                    window_count.clear()
                    count = 0
                    left = right

        return res


# @lc code=end

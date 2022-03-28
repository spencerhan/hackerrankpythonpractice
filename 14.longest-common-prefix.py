#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = list(min(strs, key = len))
        for k, c in enumerate(strs):
            for i, v in enumerate(c[0:len(shortest)]):
                if v != shortest[i]:
                    shortest[i : len(shortest)] = ""
                    break
        return ''.join(shortest)
                
            
# @lc code=end
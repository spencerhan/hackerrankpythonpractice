#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
from tokenize import group


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prevG, curG, ans = 0, 1, 0
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prevG, curG)
                prevG, curG = curG, 1 # resetting current group to 1, as new group coming in
            else:
                curG += 1
        return ans + min(prevG, curG)
# @lc code=end


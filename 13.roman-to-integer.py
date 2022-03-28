#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        normalCase = {"I": 1, "V": 5, "X": 10,
                      "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        if "CM" in s:
            s = s.replace("CM", "DCD")
        if "CD" in s: 
            s = s.replace("CD", "CCCC")
        if "XC" in s:
            s = s.replace("XC", "LXL")
        if "XL" in s:
            s = s.replace("XL", "XXXX")
        if "IX" in s:
            s = s.replace("IX", "VIV")
        if "IV" in s:
            s = s.replace("IV", "IIII")
        for c in s:
            result = result + normalCase[c]
        return result
        
# @lc code=end

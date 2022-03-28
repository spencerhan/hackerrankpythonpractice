#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = {}
        for c, v in enumerate(nums):
            if target - v not in candidates.keys():
                candidates[v] = c
            else:
                return [candidates[target - v], c]
# @lc code=end
#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def recurse(node): #use a inner method to modify the global variable
            if (node):
                if low <= node.val <= high:
                    self.ans += node.val
                if node.val > low: # use separate if statement to include all testing cases.
                    recurse(node.left)
                if node.val < high:
                    recurse(node.right)
        self.ans = 0  #create a global variable
        recurse(root)
        return self.ans
# @lc code=end


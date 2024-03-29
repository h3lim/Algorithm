# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and
                    dfs(left.left, right.right)
                    and dfs(left.right,right.left))

        return dfs(root.left,root.right)


Solution = Solution()

root = TreeNode(1,TreeNode(2,TreeNode(3, None,None), TreeNode( 4,None, None)), TreeNode( 2, TreeNode( 4, None, None), TreeNode( 3, None, None)))

Solution.isSymmetric(root)



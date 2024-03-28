import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if root == None:
            return 0
        q = collections.deque()
        q.append(root)

        while q:
            level = len(q)
            ans += 1
            for i in range(level):
                node = q.popleft()

                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)

        return ans
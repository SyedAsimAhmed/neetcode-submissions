# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            depth = 1

        # count = 1
        # leftdepth = leftdepth + maxDepth(root.left)
        # rightdepth = rightdepth + maxDepth(root.right)

        # if root.left is None and root.right is None:
        #     leftdepth = 0
        #     rightdepth = 0

        if root.left:
            leftdepth = 1
        else:
            leftdepth = 0

        if root.right:
            rightdepth = 1
        else:
            rightdepth = 0

        leftdepth = depth + self.maxDepth(root.left)
        rightdepth = depth + self.maxDepth(root.right)

        depth = max(leftdepth, rightdepth)

        return depth
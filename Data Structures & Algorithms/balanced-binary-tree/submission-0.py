# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.flag = True
        
        # def dfs(curr):
        #     if not curr:
        #         return False
            
        #     left = dfs(curr.left)
        #     right = dfs(curr.right)

        #     diff = abs(left - right) 

        #     if diff > 2:
        #         return False
        
        def dfs(curr):  
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            print(left, right)

            self.flag = self.flag and (abs(left - right) < 2)
            
            return 1 + max(left, right)
        
        dfs(root)
        return self.flag




        
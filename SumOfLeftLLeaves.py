class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def helperFunction(root):
            if root is None:
                return
            
            # Check left leaf
            if root.left and root.left.left is None and root.left.right is None:
                self.ans += root.left.val
            
            helperFunction(root.left)
            helperFunction(root.right)
        
        helperFunction(root)
        return self.ans
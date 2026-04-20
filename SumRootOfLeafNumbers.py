class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def sumNodes(root, temp):
            if root is None:
                return
            
            if root.left is None and root.right is None:
                temp += str(root.val)
                self.ans += int(temp)
                return
            
            sumNodes(root.left, temp + str(root.val))
            sumNodes(root.right, temp + str(root.val))
        
        sumNodes(root, "")
        return self.ans
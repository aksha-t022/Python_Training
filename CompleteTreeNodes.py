class Solution:
    def countNodes(self, root):
        
        def getLeftHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        def getRightHeight(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height
        
        if not root:
            return 0
        
        lh = getLeftHeight(root)
        rh = getRightHeight(root)
        
        # If perfect tree
        if lh == rh:
            return (1 << lh) - 1   # 2^h - 1
        
        # Otherwise recurse
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
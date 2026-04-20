class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        tempAns = []
        dq = deque([root, None])
        while dq:
            temp = dq.popleft()

            if temp is None:
                ans.append(tempAns[:]) 
                tempAns.clear()
                if dq:
                    dq.append(None)
            else:
                tempAns.append(temp.val)
                if temp.left:
                    dq.append(temp.left)
                if temp.right:
                    dq.append(temp.right)
        return ans
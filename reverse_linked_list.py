class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        p = None 
        while head:
            temp = head
            head = head.next
            temp.next = p
            p = temp
        return p
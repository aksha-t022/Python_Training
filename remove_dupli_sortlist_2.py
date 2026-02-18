class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        prev = None
        while t:
            if t.next and t.val==t.next.val:
                v = t.val
                while t and t.val ==v:
                    t = t.next
                if prev:
                    prev.next = t
                else:
                    head = t
            else:
                prev = t
                t=t.next
        return head
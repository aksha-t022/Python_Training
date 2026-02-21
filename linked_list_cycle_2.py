class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sp = fp = head
        while fp:
            sp = sp.next
            if fp.next == None:
                return None
            fp = fp.next.next
            if sp == fp:
                break
        if sp == fp:
            sp = head 
            while (sp != fp):
                sp = sp.next
                fp = fp.next
            return fp
        return None
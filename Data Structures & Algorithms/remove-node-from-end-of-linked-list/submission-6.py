# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        
        print(length)
        remove = length - n
        if length == 1:
            return None
        elif remove == 0:
            return head.next
        currlen = 0
        curr = prev = head
        while curr:
            if(currlen == remove):
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            currlen += 1
        return head


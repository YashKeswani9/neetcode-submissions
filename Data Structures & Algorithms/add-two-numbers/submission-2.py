# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()
        carry = 0

        while l1 or l2:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            print(l1val)
            print(l2val)
            result = l1val + l2val + carry
            print(result)
            if result > 9:
                carry = result//10
            else: 
                carry = 0
            
            dummy.next = ListNode(result%10)
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if result > 9:
            dummy.next = ListNode(carry)
        return head.next
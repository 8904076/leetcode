# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def recursive(n1, n2, carry = 0):
            if n1==None and n2==None:
                return ListNode(1) if carry == 1 else None
            if n1==None :
                n1,n2=n2,n1
                return recursive(n1, None ,carry)
            if n2==None:
                carry,n1.val=divmod((n1.val+carry),10)
                n1.next = recursive(n1.next,None,carry)
                return n1
            carry,n1.val=divmod((n1.val+n2.val+carry),10)
            n1.next=recursive(n1.next,n2.next,carry)
            return n1
        return recursive(l1,l2)
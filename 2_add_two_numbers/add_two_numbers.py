

# Approach 1: Recursive

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        # 0.
        if not l1 and not l2 and not c:
            return null

        # 1.
        sum = l1.val + l2.val + c
        # 2.
        c = sum // 10

        # 3.
        node = ListNode(sum % 10)

        # 4.
        if (l1.next != None or l2.next != None or c != 0):
            # 5.
            if l1.next == None:
                l1.next = ListNode(0)
            # 6.
            if l2.next == None:
                l2.next = ListNode(0)
            # 7.
            node.next = self.addTwoNumbers(l1.next, l2.next, c)
        # 8.
        return node


# Approach 2: Iterative
class Solution:
    def addTwoNumbers(self, l1, l2):
        # 0.
        dummy = cur = ListNode(0)
        c = 0

        # 1.
        while l1 or l2 or c:

            # 2.
            if l1:
                c += l1.val
                l1 = l1.next

            # 3.
            if l2:
                c += l2.val
                l2 = l2.next

            # 4.
            cur.next = ListNode(c % 10)
            # 5.
            cur = cur.next
            # 6.
            c //= 10

        # 7.
        return dummy.next


# Notes

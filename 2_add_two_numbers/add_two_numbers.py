

# Approach 1: Recursive

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        # 0. First we check if either _l1_, _l2_, or _c_ is undefined
        if not l1 and not l2 and not c:
            return null

        # 1. Then we sum values of both linked lists and the _c_ that was carried over
        sum = l1.val + l2.val + c
        # 2. Equal _c_ to _sum_ divided by 10 which should equal 1 and carry over if _sum_ is 10
        c = sum // 10

        # 3. We then store _sum_ modulus 10 in the _ListNode_
        node = ListNode(sum % 10)

        # 4. Conditional whether if either linked list has a next value or _c_ has a value
        if (l1.next != None or l2.next != None or c != 0):
            # 5. If next of _l1_ is none then give it a value of 0 so we can continue iterating. Useful if both linked lists are different lengths
            if l1.next == None:
                l1.next = ListNode(0)
            # 6. Do same as step 6 but with _l2_
            if l2.next == None:
                l2.next = ListNode(0)
            # 7. Recursive calling itself with updated values and equaling result to next value of linked list to return
            node.next = self.addTwoNumbers(l1.next, l2.next, c)
        # 8. When everything is done return tail of result linked list
        return node


# Approach 2: Iterative
class Solution:
    def addTwoNumbers(self, l1, l2):
        # 0. First we initialize variables: _dummy_ and _cur_ to head of ListNode and _cur_ to 0
        dummy = cur = ListNode(0)
        c = 0

        # 1. Then we iterate while _l1_, _l2_, or _c_ are still not null
        while l1 or l2 or c:

            # 2. During each iteration we check if _l1_ has a value then add that value to c and iterative to next _l1_
            if l1:
                c += l1.val
                l1 = l1.next

            # 3. We do the same as above step 3 but for _l2_ now
            if l2:
                c += l2.val
                l2 = l2.next

            # 4. Now we give the next of _cur_ the value of the remainder of _c_ divided by 10
            cur.next = ListNode(c % 10)
            # 5. Move cur to the next position
            cur = cur.next
            # 6. Change value of _c_ to _c_ divided by 10 which should equal 1 if _c_ was 10 and 0 if it wasn't
            c //= 10

        # 7. When everything is done return tail of result linked list
        return dummy.next

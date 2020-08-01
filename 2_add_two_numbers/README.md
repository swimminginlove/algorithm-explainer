# Add Two Numbers

### Link: https://leetcode.com/problems/add-two-numbers/

## Problem statement:

```
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

## Explanation:

Ok, so we're going to be covering two approaches for solving this problem.

### Approach 1:

0. First we check if either _l1_, _l2_, or _c_ is undefined
1. Then we sum values of both linked lists and the _c_ that was carried over
2. Equal _c_ to _sum_ divided by 10 which should equal 1 and carry over if _sum_ is 10
3. We then store _sum_ modulus 10 in the _ListNode_
4. Conditional whether if either linked list has a next value or _c_ has a value
5. If next of _l1_ is none then give it a value of 0 so we can continue iterating. Useful if both linked lists are different lengths
6. Do same as step 6 but with _l2_
7. Recursive calling itself with updated values and equaling result to next value of linked list to return
8. When everything is done return tail of result linked list

### Approach 2:

0. First we initialize variables: _dummy_ and _cur_ to head of ListNode and _cur_ to 0
1. Then we iterate while _l1_, _l2_, or _c_ are still not null
2. During each iteration we check if _l1_ has a value then add that value to c and iterative to next _l1_
3. We do the same as above step 3 but for _l2_ now
4. Now we give the next of _cur_ the value of the remainder of _c_ divided by 10
5. Move cur to the next position
6. Change value of _c_ to _c_ divided by 10 which should equal 1 if _c_ was 10 and 0 if it wasn't
7. When everything is done return tail of result linked list

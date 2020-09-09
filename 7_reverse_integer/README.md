# Reverse Integer

### Link: https://leetcode.com/problems/reverse-integer/

## Problem statement:

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

```
Input: 123
Output: 321
```

Example 2:

```
Input: -123
Output: -321
```

Example 3:

```
Input: 120
Output: 21
```

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

## Explanation:

### Approach 1: Converting to and reversing a string

0. Get absolute value of _x_ and convert to string
1. Reverse string using slice syntax by not setting start or end index but setting -1 as step value then converting to number
2. Check if reversed number is within 32 bit range
3. If _x_ was negative then negate _reversed_ before returning
4. Return _reversed_

### Approach 2: Reversing integer

0. Initialize variables: _result_ will hold reverse value, _symbol_ will hold negative if _x_ is a negative number
1. Handle if _x_ is a negative number
2. Reversing _x_ by doing modulo division and adding value to result\*10
3. Check _result_ is in 32 bit range
4. Negate result if _x_ was negative

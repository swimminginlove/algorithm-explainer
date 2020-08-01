# Palindrome Number

### Link: https://leetcode.com/problems/palindrome-number/

## Problem statement:

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

```
Input: 121
Output: true
```

Example 2:

```
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

Example 3:

```
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

Follow up:

Coud you solve it without converting the integer to a string?

## Explanation:

### Approach 1:

0. Initialize _original_ and _backwards_ variables
1. Iterate while _x_ is greater than 0
2. Sort of "append" values from _x_ onto the _backwards_ variable by one-by-one pulling them off _x_ with the "x % 10", and adding them to backwards \* 10
3. Sort of "pop" values from end of _x_ using "x // 10" since it discards remainder values from the division. This makes it so that the "x % 10" in step 2 has a new value on each iteration
4. Return whether _original_ and _backwards_ are equal (_x_ is palindromic)

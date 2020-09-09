# String to Integer

### Link: https://leetcode.com/problems/string-to-integer-atoi/

## Problem statement:

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

```
Input: "42"
Output: 42
```

Example 2:

```
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
```

Example 3:

```
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
```

Example 4:

```
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
```

Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
Thefore INT_MIN (−231) is returned.

## Explanation:

### Approach 1:

0. Initialize variables
1. Strip _s_ string of whitespace and convert to array(list)
2. If array is empty then return
3. If array has sign in front then note the sign and delete it
4. Iterate while _i_ is less than _arr_ array and _arr[i]_ is a digit
5. Convert digits one by one using modulus and adding to result \* 10. (4879) 4 > 48 > 487 > 4879. Get ascii value of character at index _i_ of array _arr_. Also 48 is ord('0').
6. Multiply _result_ by sign of input _s_
7. CCheck if _result_ is less than or greater than +/- 2\*\*32 and return

# Longest Palindromic Substring

### Link: https://leetcode.com/problems/longest-palindromic-substring/

## Problem statement:

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

Example 2:

```
Input: "cbbd"
Output: "bb"
```

## Explanation:

A palindrome mirrors around its center and so we can determine a palindrome by expanding from a center and verifying both sides mirror each other

Because a center point can contain both 1 or 2 items. We're going to have to handle both cases separately.

### Approach 1:

0. Initialize variables
1. Iterate over the range of the length of _s_
2. Pass same _i_ for _l_ and _r_ to _expander_ function this way the _expander_ function handles the odd case Ex. b > aba > cabac > ...
3. If returned value, _odd_, is greater than current max, _result_, then set _result_ to _odd_
4. Pass different _i_ for _l_ and _r_ to _expander_ function so the _expander_ function handles the even case Ex. aa > baab > abaaba > ...
5. If returned value, _even_, is greater than current max, _result_, then set _result_ to _even_
6. Return _result_

#### _expander_ function explanation

_l_ and _r_ are the middle indexes of the possible palindrome we're checking out

0. Iterate while _l_ is greater than or equal to 0 AND _r_ is less than the length of _s_ AND the _l_th index of \_s_ is equal to the _r_th index of \_s_
1. Move the left border out by decrementing _l_ by one AND move the right border out by incrementing _r_
2. Return the range of string _s_ from beginning _l_ to end _r_

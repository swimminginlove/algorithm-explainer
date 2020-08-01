# Longest Substring Without Repeating Characters

### Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Problem statement:

Given a string, find the length of the longest substring without repeating characters.

Example 1:

```
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

Example 2:

```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

Example 3:

```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Explanation:

I only got one approach for this. If you guys would like to contribute other approaches that would be awesome!! You're helping us all out by contributing!

### Approach 1:

0. Initialize _seen_ window and _max_length_
1. Iterate over input string s
2. If _c_ is in the _seen_ window then move beginning index of _s_ 1 to the right of the index of _c_
3. Add _c_ to seen window
4. Check if current size of window is bigger than previous _max_length_ and change _max_length_ if so
5. Return _max_length_

# Two sum

### Link: https://leetcode.com/problems/two-sum/

## Problem statement:

```
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## Explanation:

Ok, so we're going to be covering three approaches for solving this problem.

### Approach 1:

The first approach is a brute force solution.

0. First we iterate over the range of every item, _i_, in the _nums_ array
1. Then we iterate over the range of every item, _j_, in the _nums_ array
2. Lastly, we check if the elements at the ith and jth indexes of the _nums_ array add up to _target_ and return an array of said indexes if they do

### Approach 2:

The second approach is called the "two-pass hash table" approach because we're going to iterate over the given array twice and, in the process, fill and query a hash table.

0. Initialize the _hash_ table
1. Iterate over the _nums_ array and populate the hash table with values from the _nums_ array as keys and their indexes as values
2. Iterate over the _nums_ array and get the result of _target_ minus each value and equal it to _n_
3. Check if _n_ is in the _hash_ table as well as that the index returned from the _hash_ table isn't the same as _i_ (we're not doubling the same number)

### Approach 3:

The third approach is just an improvement on the second approach. With the third approach, instead of iterating on our input array, _nums_, two separate times, now we're iterating only once.

0. Initialize the _hash_ table
1. Iterate over the _nums_ array and get the result of _target_ minus each value and equal it to _n_
2. If _n_ is not in the _hash_ table then add it to the _hash_ table.
3. If _n_ is in the _hash_ table then that means you found your answer, indexes of two numbers that add up to the _target_. Return an array of two indexes.

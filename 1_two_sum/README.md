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

Ok, so we're going to be coverying three approaches to solving this problem.

### Approach 1:

The first approach is that of brute force.
For every item, i, in the given array, we're going to iterate over every item, j, in the given array starting from i. Then we're going to check if i + j equals the target number and return the indices if they do.

For example...
First we'll start with 2 in the above array then we'll check to see if two plus any of the other numbers in the above array equals the given target value. If we don't find a match then we'll do the same thing with 7, comparing it to every number in the above array. No match? Then let's check 11... and so on...

Of course with the above array we find our match pretty early on with 2 and 7 but that's just luck!

This approach, though simple, is very ineffecient which is why I'm super !EXCITED! about approaches 2 and 3!!

Onward!

### Approach 2:

Now, this is where things get interesting. The second approach is called the "two-pass hash table" approach because we're going to iterate over the given array twice and, in the process, fill and query a hash table.

To create the hash table we're going to use a python dictionary.

Then we're going to iterate over the input array _nums_ and for every iteration we're going to store the value of the array into the hash table.

Now, we're going to iterate over the input array a second time but now, with each iteration, we're going to query the hash table to see if our _target_ number minus the the current value in the array at that iteration is in the hash table. If it is in the hash table then that means we've found our answer.

### Approach 3:

The third approach is just an improvement on the second approach. With the third approach, instead of iterating on our input array, _nums_, two separate times, now we're iterating only once.

In this approach, we create our hash table like before. Then we iterate over our input array _nums_, and during each iteration we first calculate the value of target minus the current _num_ in the array. Then we check if that value is in the hash table. If it isn't, then we add it to the hash table. If it is, then that means we've just found our answer.

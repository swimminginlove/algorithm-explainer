# https://leetcode.com/problems/two-sum/
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


# Approach 1: Brute force
def twoSum(nums, target):
    for x in range(len(nums)):
        for y in range(len(nums)):
            if nums[x] + nums[y] == target:
                return [x, y]


print(twoSum(nums=[2, 7, 11, 15], target=9))


# Approach 2: Two-pass Hash table
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            seen[num] = i
        for i, num in enumerate(nums):
            n = target - num
            if n in seen:
                return [seen[n], i]


# Approach 3: One-pass Hash table
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in seen:
                seen[num] = i
            else:
                return [seen[n], i]

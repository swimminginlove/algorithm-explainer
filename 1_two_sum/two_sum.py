# Approach 1: Brute force
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Approach 2: Two-pass Hash table
class Solution:
    def twoSum(self, nums, target):
        hash = {}
        for i, num in enumerate(nums):
            hash[num] = i
        for i, num in enumerate(nums):
            n = target - num
            if n in hash and hash[n] is not i:
                return [hash[n], i]


# Approach 3: One-pass Hash table
class Solution:
    def twoSum(self, nums, target):
        hash = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in hash:
                hash[num] = i
            else:
                return [hash[n], i]

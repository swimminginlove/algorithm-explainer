# Approach 1: Brute force
class Solution:
    def twoSum(self, nums, target):
        # 0.
        for i in range(len(nums)):
            # 1.
            for j in range(i+1, len(nums)):
                # 2.
                if nums[i] + nums[j] == target:
                    return [i, j]


# Approach 2: Two-pass Hash table
class Solution:
    def twoSum(self, nums, target):
        # 0.
        hash = {}
        # 1.
        for i, num in enumerate(nums):
            hash[num] = i
        # 2.
        for i, num in enumerate(nums):
            n = target - num
            # 3.
            if n in hash and hash[n] is not i:
                return [hash[n], i]


# Approach 3: One-pass Hash table
class Solution:
    def twoSum(self, nums, target):
        # 0.
        hash = {}
        # 1.
        for i, num in enumerate(nums):
            n = target - num
            # 2.
            if n not in hash:
                hash[num] = i
            # 3.
            else:
                return [hash[n], i]

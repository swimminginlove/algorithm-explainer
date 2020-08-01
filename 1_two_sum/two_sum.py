# Approach 1: Brute force
class Solution:
    def twoSum(self, nums, target):
        # 0. First we iterate over the range of every item, _i_, in the _nums_ array
        for i in range(len(nums)):
            # 1. Then we iterate over the range of every item, _j_, in the _nums_ array
            for j in range(i+1, len(nums)):
                # 2. Lastly, we check if the elements at the ith and jth indexes of the _nums_ array add up to _target_ and return an array of said indexes if they do
                if nums[i] + nums[j] == target:
                    return [i, j]


# Approach 2: Two-pass Hash table
class Solution:
    def twoSum(self, nums, target):
        # 0. Initialize the _hash_ table
        hash = {}
        # 1. Iterate over the _nums_ array and populate the hash table with values from the _nums_ array as keys and their indexes as values
        for i, num in enumerate(nums):
            hash[num] = i
        # 2. Iterate over the _nums_ array and get the result of _target_ minus each value and equal it to _n_
        for i, num in enumerate(nums):
            n = target - num
            # 3. Check if _n_ is in the _hash_ table as well as that the index returned from the _hash_ table isn't the same as _i_ (we're not doubling the same number)
            if n in hash and hash[n] is not i:
                return [hash[n], i]


# Approach 3: One-pass Hash table
class Solution:
    def twoSum(self, nums, target):
        # 0. Initialize the _hash_ table
        hash = {}
        # 1. Iterate over the _nums_ array and get the result of _target_ minus each value and equal it to _n_
        for i, num in enumerate(nums):
            n = target - num
            # 2. If _n_ is not in the _hash_ table then add it to the _hash_ table.
            if n not in hash:
                hash[num] = i
            # 3. If _n_ is in the _hash_ table then that means you found your answer, indexes of two numbers that add up to the _target_. Return an array of two indexes.
            else:
                return [hash[n], i]

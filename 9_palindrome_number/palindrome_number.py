class Solution:
    def isPalindrome(self, x):
        # 0. Initialize _original_ and _backwards_ variables
        original = x
        backwards = 0
        # 1. Iterate while _x_ is greater than 0
        while x > 0:
            # 2. Sort of "append" values from _x_ onto the _backwards_ variable by one-by-one pulling them off _x_ with the "x % 10", and adding them to backwards \* 10
            backwards = backwards * 10 + x % 10
            # 3. Sort of "pop" values from end of _x_ using "x // 10" since it discards remainder values from the division. This makes it so that the "x % 10" in step 2 has a new value on each iteration
            x = x // 10
        # 4. Return whether _original_ and _backwards_ are equal (_x_ is palindromic)
        return original == backwards

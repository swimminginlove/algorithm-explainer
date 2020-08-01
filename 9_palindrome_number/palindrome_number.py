class Solution:
    def isPalindrome(self, x):
        # 0.
        original = x
        backwards = 0
        # 1.
        while x > 0:
            # 2.
            backwards = backwards * 10 + x % 10
            # 3.
            x = x // 10
        # 4.
        return original == backwards

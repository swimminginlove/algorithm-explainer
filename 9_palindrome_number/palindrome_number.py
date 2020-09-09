class Solution:
    def isPalindrome(self, x):
        # 0.
        original = x
        reversed = 0
        # 1.
        while x > 0:
            # 2.
            reversed = reversed * 10 + x % 10
            # 3.
            x = x // 10
        # 4.
        return original == reversed

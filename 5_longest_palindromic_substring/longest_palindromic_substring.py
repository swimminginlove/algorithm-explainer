
class Solution:
    def longestPalindrome(self, s):
        # 0.
        result = ""
        # 1.
        for i in range(len(s)):
            # 2.
            odd = self.helper(s, i, i)
            # 3.
            if len(odd) > len(result):
                result = odd

            # 4.
            even = self.helper(s, i, i+1)
            # 5.
            if len(even) > len(result):
                result = even
        # 6.
        return result

    def helper(self, s, l, r):
        # 0.
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # 1.
            l -= 1
            r += 1
        # 2.
        return s[l+1:r]

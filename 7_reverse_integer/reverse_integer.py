# Approach 1:
class Solution:
    def reverse(self, x):
        # 0.
        s = str(abs(x))

        # 1.
        reversed = int(s[::-1])
        # reversed = int(s[len(s):-len(s)-1:-1])

        # 2.
        if reversed > 2147483647:
            return 0

        # 3.
        if x < 0:
            reversed *= -1
        # 4.
        return reversed

# Approach 2:


class Solution:
    def reverse(self, x):
        # 0.
        result = 0
        symbol = 1

        # 1.
        if x < 0:
            symbol = -1
            x = -x

        # 2.
        while (x):
            result = result * 10 + x % 10
            x //= 10

        # 3.
        if result > pow(2, 31):
            return 0

        # 4.
        else:
            return result * symbol

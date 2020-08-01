# Approach 1:
class Solution:
    def reverse(self, x):
        # 0.
        s = str(abs(x))

        # 1.
        reversed = int(s[::-1])

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
        result = 0
        symbol = 1

        if x < 0:
            symbol = -1
            x = -x

        while (x):
            result = result * 10 + x % 10
            x //= 10

        if result > pow(2, 31):
            return 0
        else:
            return result * symbol

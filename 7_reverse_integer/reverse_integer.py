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
        # Initialize variables: result will hold reverse value, symbol will hold negative if _x_ is negative number
        result = 0
        symbol = 1

        # Handle if _x_ is negative number
        if x < 0:
            symbol = -1
            x = -x

        # Reverseing _x_ by doing modulo division and adding value to result*10
        while (x):
            result = result * 10 + x % 10
            x //= 10

        # Check result is in 2**32 range
        if result > pow(2, 31):
            return 0

        # Negate result if _x_ was negative
        else:
            return result * symbol

# Approach 1:
class Solution:
    def reverse(self, x):
        # 0. Get absolute value of _x_ and convert to string
        s = str(abs(x))

        # 1. Reverse string using slice syntax by not setting start or end index
        # but setting -1 as step value then converting to number
        reversed = int(s[::-1])
        # reversed = int(s[len(s):-len(s)-1:-1])

        # 2. Check if reversed number is within 32 bit range
        if reversed > 2147483647:
            return 0

        # 3. If _x_ was negative then negate _reversed_ before returning
        if x < 0:
            reversed *= -1
        # 4. Return _reversed_
        return reversed

# Approach 2:


class Solution:
    def reverse(self, x):
        # Initialize variables:
        # result will hold reverse value
        # symbol will hold negative if _x_ is negative number
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

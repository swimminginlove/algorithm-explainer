

# Approach 1
class Solution(object):
    def myAtoi(self, s):

        # 0.
        result = 0
        i = 0

        # 1.
        arr = list(s.strip())

        # 2.
        if len(arr) == 0:
            return 0

        # 3.
        if arr[0] == '-':
            sign = -1
            i = 1
            # or del arr[0]

        elif arr[0] == '+':
            sign = 1
            i = 1
            # or del arr[0]

        else:
            sign = 1

        # 4.
        while i < len(arr) and arr[i].isdigit():
            # 5.
            result = result*10 + ord(arr[i]) - 48
            i += 1

        # 6.
        result = result * sign

        # 7.
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        else:
            return result

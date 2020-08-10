

class Solution(object):
    def myAtoi(self, s):

        # initialize variables:
        # result which will contain result which we'll return
        # i which we'll use to iterate
        result = 0
        i = 0

        # strip _s_ string of whitespace and convert to array(list)
        arr = list(s.strip())

        # If array is empty then return
        if len(arr) == 0:
            return 0

        # if array has sign in front then note the sign
        if arr[0] == '-':
            sign = -1
        else:
            sign = 1

        # if array has a sign in front then we need to delete the sign from array
        if arr[0] == '-' or arr[0] == '+':
            del arr[0]
            # or i = 1

        # Iterate while i is less than arr array and arr[i] is a digit
        while i < len(arr) and arr[i].isdigit():
            # convert digits one by one using modulus and adding to result * 10
            # (4879) 4 > 48 > 487 > 4879
            # We could do int(arr[i]) but int conversion is slower. Also 48 is ord('0')
            result = result*10 + ord(arr[i]) - 48
            i += 1  # increment i

        # multiply result by sign of s
        result = result * sign

        # check if result less than or greater than +/- 2**32
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        else:
            return result

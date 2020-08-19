

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

        # if array has sign in front then note the sign and delete it
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

        # Iterate while _i_ less than _arr_ array and _arr[i]_ is a digit
        while i < len(arr) and arr[i].isdigit():
            # convert digits one by one using modulus and adding to result * 10
            # (4879) 4 > 48 > 487 > 4879
            # We could do int(arr[i]) but int conversion is slower. Also 48 is ord('0')

            #print("result: ", result, "arr[i]: ", arr[i])

            # get ascii value of character at index _i_ of array _arr_.
            # Also 48 is ord('0')
            result = result*10 + ord(arr[i]) - 48
            # increment i
            i += 1

        # multiply _result_ by sign of input _s_
        result = result * sign

        # check if _result_ less than or greater than +/- 2**32
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        else:
            return result

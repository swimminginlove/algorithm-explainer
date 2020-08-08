

'''
A palindrome mirrors around its center and so we can determine a palindrome by expanding from a center and verifying both sides mirror each other

Because a center point can contain both 1 or 2 items. We're going to have to handle both cases separately.
'''


class Solution:
    def longestPalindrome(self, s):
        # 0. Initialize result variable which will contain *longest palindromic substring* that we will return
        result = ""

        # 1. Iterate over the range of the length of s
        for i in range(len(s)):

            # 2. Pass same _i_ for _l_ and _r_ to _expander_ function.
            # Center is single value.
            # Odd case
            # b > aba > cabac > ...
            odd = self.expander(s, i, i)

            # 3. If _odd_ is greater than our current max, _result_, then set _result_ to _odd_
            if len(odd) > len(result):
                result = odd

            # 4. Pass different _i_ for _l_ and _r_ to _expander_ function.
            # Center is two values
            # Even case
            # aa > baab > abaaba > ...
            even = self.expander(s, i, i+1)

            # 5. If _even_ is greater than our current max, _result_, then set _result_ to _even_
            if len(even) > len(result):
                result = even

        # 6. Return _result_
        return result

    def expander(self, s, l, r):
        # 0. Iterate while
        # _l_ is greater than or equal to 0
        # AND _r_ is less than the length of _s_
        # AND the _l_th index of _s_ is equal to the _r_th index of _s_

        while l >= 0 and r < len(s) and s[l] == s[r]:
            # 1. Move the left border out by decrementing _l_ by one
            # AND move the right border out by incrementing _r_
            l -= 1
            r += 1

        # 2. Return the range of string _s_ from beginning _l_ to end _r_
        return s[l+1:r]


# Approach 1:


class Solution:
    def lengthOfLongestSubstring(self, s):

        # 0.
        seen = ''
        max_length = 0

        # 1.
        for c in s:
            # 2.
            if c in seen:
                seen = seen[seen.index(c)+1:]

            # 3.
            seen += c
            # 4.
            max_length = max(max_length, len(seen))

        # 5.
        return max_length

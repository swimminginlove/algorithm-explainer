
# Approach 1:


class Solution:
    def lengthOfLongestSubstring(self, s):

        # 0. Initialize _seen_ window and _max_length_
        seen = ''
        max_length = 0

        # 1. Iterate over input string s
        for c in s:
            # 2. If _c_ is in the _seen_ window then move beginning index of _seen_ 1 to the right of the index of _c_
            if c in seen:
                seen = seen[seen.index(c)+1:]

            # 3. Add _c_ to seen window
            seen += c
            # 4. Check if current size of window is bigger than previous _max_length_ and change _max_length_ if so
            max_length = max(max_length, len(seen))

        # 5. Return _max_length_
        return max_length

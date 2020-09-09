

class Solution:
    def convert(self, s, numRows):
        # 0.
        if numRows <= 1:
            return s

        # 1.
        lines = [""] * numRows
        row = 0
        step = 1

        # 2.
        for char in s:

            # 3.
            lines[row] += char

            # 4.
            if row == 0:
                step = 1
            elif row == numRows-1:
                step = -1

            # 5.
            row += step

        # 6.
        return "".join(lines)

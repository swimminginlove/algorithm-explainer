class Solution:
    def convert(self, s, numRows):
        # 0.
        if numRows <= 1:
            return s

        # 1.
        lines = [""] * numRows
        index = 0
        step = 1

        # 2.
        for i in s:
            # 3.
            lines[index] += i
            # 4.
            index += step
            # 5.
            if index == 0 or index == numRows - 1:
                step = step * -1
        # 6.
        return "".join(lines)

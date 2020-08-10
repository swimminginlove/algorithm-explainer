# the zigzag pattern is just a pictorial image for us to have a better understanding
# What the trick of algorithm is actually add the next char of the given string to different rows.
# Don't really think how to move the cursor in the matrix.
# It's really misleading way you think of this.


# Example: if nRows = 5, then row iterates through 0 1 2 3 4 3 2 1 0 1 2 3 4 3 2... etc. Like a zigzag!


class Solution:
    def convert(self, s, numRows):
        # 0. Return _s_ if _numRows_ less than or equal to 1
        if numRows <= 1:
            return s

        # 1. Intialize variables:
        # _lines_ array with same number of elements as _numRows_
        # the _row_ at which we add a letter
        # and _step_ which determines whether we go up(negative) or down(positive)
        lines = [""] * numRows
        row = 0
        step = 1

        # 2. Iterate over _s_
        for char in s:
            print("lines: ", lines)

            # 3. Add letter, _char_, to _lines_
            lines[row] += char

            # 4. Determine whether going down or up
            if row == 0:
                step = 1  # going down
            elif row == numRows-1:
                step = -1  # going up

            # 5. Add _step_ to _row_
            row += step

        # 6. Return all the elements in the _lines_ array joined
        return "".join(lines)


# convert("PAYPALISHIRING", 3)

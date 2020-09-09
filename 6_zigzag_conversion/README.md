# ZigZag Conversion

### Link: https://leetcode.com/problems/zigzag-conversion/

## Problem statement:

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

Example 1:

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

Example 2:

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```

## Explanation:

This problem doesn't have anything to do with moving a cursor in a matrix. The zigzag pattern is just a pictorial image. All we're going to do is iterate and add the characters to specific rows.

If numRows = 5, then row iterates through 0 1 2 3 4 3 2 1 0 1 2 3 4 3 2... Like a zigzag!

### Approach 1:

0. Return _s_ if _numRows_ less than or equal to 1
1. Intialize variables: _lines_ array with same number of elements as _numRows_, the _row_ at which we add a letter, and _step_ which determines whether we go up(negative) or down(positive)
2. Iterate over _s_
3. Add letter to _lines_ array
4. Determine whether going down or up. When _row_ is 0, go down. When _row_ is \_numRows-1, go up.
5. Add _step_ to _row_
6. Return all the elements in the _lines_ array joined

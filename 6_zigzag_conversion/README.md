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

### Approach 1:

0. Return _s_ if _numRows_ less than or equal to 1
1. Intialize variables: _lines_ array with same number of elements as _numRows_, the _index_ at which we add a letter, and _step_ which determines whether we go up(positive) or down(negative)
2. Iterate over _s_
3. Add letter, _i_, to _lines_
4. Add _step_ to _index_
5. If _index_ is 0 or _index_ is equal to _numRows_ minus 1 then negate _step_
6. Return all the elements in the _lines_ array joined

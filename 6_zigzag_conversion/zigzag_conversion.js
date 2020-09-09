/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
  // 0.
  if (numRows <= 1) {
    return s;
  }

  // 1.
  var lines = [];
  for (let i = 0; i < numRows; i++) lines.push("");
  // for (let i = 0; i < numRows; i++) lines[i] = [];
  var row = 0;
  var step = 1;

  // 2.
  for (let i = 0; i < s.length; i++) {
    // 3.
    lines[row] += s[i];

    // 4.
    if (row == 0 || row == numRows - 1) {
      step = step * -1;
    }

    // 5.
    row += step;
  }
  // 6.
  return lines.join("");
};

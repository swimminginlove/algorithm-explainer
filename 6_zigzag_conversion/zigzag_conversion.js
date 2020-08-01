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
  var index = 0;
  var step = 1;

  // 2.
  for (let i = 0; i < s.length; i++) {
    // 3.
    lines[index] += s[i];
    // 4.
    index += step;
    // 5.
    if (index == 0 || index == numRows - 1) {
      step = step * -1;
    }
  }
  // 6.
  return lines.join("");
};

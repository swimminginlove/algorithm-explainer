// Approach 1:
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  // 0.
  var s = Math.abs(x).toString();
  // 1.
  var reversed = parseInt(s.split("").reverse().join(""));
  // 2.
  if (reversed > 2147483647) {
    return 0;
  }
  // 3.
  if (x < 0) {
    reversed *= -1;
  }
  // 4.
  return reversed;
};

// Approach 2:

function reverse(x) {
  // 0.
  var result = 0;
  var symbol = 1;

  // 1.
  if (x < 0) {
    symbol = -1;
    x = -x;
  }

  // 2.
  while (x > 0) {
    result = result * 10 + (x % 10);
    x = Math.trunc(x / 10);
  }

  // 3.
  if (result > 2147483647) {
    return 0;
  } else {
    // 4.
    return result * symbol;
  }
}

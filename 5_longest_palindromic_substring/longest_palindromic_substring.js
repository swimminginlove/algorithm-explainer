// Approach 1
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  // 0.
  var result = "";
  // 1.
  for (let i = 0; i < s.length; i++) {
    // 2.
    var odd = expander(s, i, i);
    // 3.
    if (odd.length > result.length) {
      result = odd;
    }
    // 4.
    var even = expander(s, i, i + 1);
    // 5.
    if (even.length > result.length) {
      result = even;
    }
  }

  // 6.
  return result;
};

function expander(s, l, r) {
  while (l >= 0 && r < s.length && s[l] === s[r]) {
    l -= 1;
    r += 1;
  }
  return s.slice(l + 1, r);
}

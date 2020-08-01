// Approach 1:
/**
 * @param {string} s
 * @return {number}
 */
function lengthOfLongestSubstring(s) {
  // 0.
  var seen = "";
  var max_length = 0;

  // 1.
  for (var i = 0; i < s.length; i++) {
    // 2.
    const c = s[i];
    const index = seen.indexOf(c);
    if (index >= 0) {
      seen = seen.substring(index + 1);
    }

    // 3.
    seen += c;

    // 4.
    max_length = Math.max(max_length, seen.length);
  }

  // 5.
  return max_length;
}

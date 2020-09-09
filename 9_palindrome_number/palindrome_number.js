var isPalindrome = function (x) {
  // 0.
  var original = x;
  var reversed = 0;

  // 1.
  while (x > 0) {
    // 2.
    reversed = reversed * 10 + (x % 10);
    // 3.
    x = Math.trunc(x / 10);
  }
  // 4.
  return original == reversed;
};

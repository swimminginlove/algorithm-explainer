var isPalindrome = function (x) {
  var original = x;
  var backwards = 0;

  while (x > 0) {
    backwards = backwards * 10 + (x % 10);
    x = Math.trunc(x / 10);
  }
  return original == backwards;
};

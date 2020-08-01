// Approach 1: Brute force
function twoSum(nums, target) {
  // 0.
  for (let i = 0; i < nums.length; i++) {
    // 1.
    for (let j = i + 1; j < nums.length; j++) {
      // 2.
      if (nums[i] + nums[j] == target) {
        return [i, j];
      }
    }
  }
}

// Approach 2: Two-pass Hash table
function twoSum(nums, target) {
  // 0.
  let hash = {};

  // 1.
  for (let i = 0; i < nums.length; i++) {
    hash[nums[i]] = i;
  }

  // 2.
  for (let i = 0; i < nums.length; i++) {
    var n = target - nums[i];
    // 3.
    if (hash[n] !== undefined && hash[n] != i) {
      return [hash[n], i];
    }
  }
  return [];
}

// Approach 3: One-pass Hash table
function twoSum(nums, target) {
  // 0.
  let hash = {};

  // 1.
  for (let i = 0; i < nums.length; i++) {
    var n = target - nums[i];
    // 2.
    if (hash[n] !== undefined) {
      return [hash[n], i];
    }
    // 3.
    hash[nums[i]] = i;
  }
  return [];
}

// Approach 1: Brute force
function twoSum(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] == target) {
        return [i, j];
      }
    }
  }
}

// Approach 2: Two-pass Hash table
function twoSum(nums, target) {
  let hash = {};

  for (let i = 0; i < nums.length; i++) {
    hash[nums[i]] = i;
  }

  for (let i = 0; i < nums.length; i++) {
    var r = target - nums[i];
    if (hash[r] !== undefined && hash[r] != i) {
      return [hash[r], i];
    }
  }
  return [];
}

// Approach 3: One-pass Hash table
function twoSum(nums, target) {
  let hash = {};

  for (let i = 0; i < nums.length; i++) {
    var r = target - nums[i];
    if (hash[r] !== undefined) {
      return [hash[r], i];
    }
    hash[nums[i]] = i;
  }
  return [];
}

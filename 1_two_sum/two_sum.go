

// Approach 1: Brute force
func twoSum(nums []int, target int) []int {
	// 0.
	for i := 0; i < len(nums); i++ {
		// 1.
		for j := i + 1; j < len(nums); j++ {
			// 2.
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return []int{}
}

// Approach 2: Two-pass Hash table
func twoSum(nums []int, target int) []int {
	// 0.
	hash := make(map[int]int)

	// 1.
	for i, num := range nums {
		hash[num] = i
	}

	// 2.
	for i, num := range nums {
		n := target - num
		// 3.
		j, ok := hash[n]
		if ok && j != i {
			return []int{j, i}
		}
	}
	return []int{}
}

// Approach 3: One-pass Hash table
func twoSum(nums []int, target int) []int {
	// 0.
	hash := make(map[int]int)
	// 1.
	for i, num := range nums {
		n := target - num
		// 2.
		j, ok := hash[n]
		if ok {
			return []int{j, i}
		} else {
			// 3.
			hash[num] = i
		}
	}
	return []int{}
}

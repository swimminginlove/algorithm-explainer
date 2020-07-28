

// Approach 1: Brute force
func twoSum(nums []int, target int) []int {
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return []int{}
}

// Approach 2: Two-pass Hash table
func twoSum(nums []int, target int) []int {
	hash := make(map[int]int)

	for i, num := range nums {
		hash[num] = i
	}

	for i, num := range nums {
		j, ok := hash[target-num]
		if ok && j != i {
			return []int{j, i}
		}
	}
	return []int{}
}

// Approach 3: One-pass Hash table
func twoSum(nums []int, target int) []int {
	hash := make(map[int]int)
	for i, num := range nums {
		j, ok := hash[target-num]
		if ok {
			return []int{j, i}
		} else {
			hash[num] = i
		}
	}
	return []int{}
}

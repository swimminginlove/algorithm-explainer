// Approach 2:

func reverse(x int) int {
	// 0.
	result := 0
	symbol := 1

	// 1.
	if x < 0 {
		symbol = -1
		x = -x
	}

	// 2.
	for x > 0 {
		result = result*10 + x%10
		x = x / 10
	}

	// 3.
	if result > 2147483647 {
		return 0
	} else {
		// 4.
		return result * symbol
	}
}
// Approach 2:

func reverse(x int) int {
	result := 0
	symbol := 1

	if x < 0 {
		symbol = -1
		x = -x
	}

	for x > 0 {
		result = result*10 + x%10
		x = x / 10
	}

	if result > 2147483647 {
		return 0
	} else {
		return result * symbol
	}
}
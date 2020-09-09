func isPalindrome(x int) bool {
	// 0.
	original := x
	reversed := 0

	// 1.
	for x > 0 {
		// 2.
		reversed = reversed*10 + x%10
		// 3.
		x = x / 10
	}

	// 4.
	return original == reversed
}

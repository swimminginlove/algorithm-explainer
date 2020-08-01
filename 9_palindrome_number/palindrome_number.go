func isPalindrome(x int) bool {
	original := x
	backwards := 0

	for x > 0 {
		backwards = backwards*10 + x%10
		x = x / 10
	}

	return original == backwards
}

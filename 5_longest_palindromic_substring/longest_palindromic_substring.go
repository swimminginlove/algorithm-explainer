func longestPalindrome(s string) string {
	// 0.
	result := ""
	// 1.
	for i := 0; i < len(s); i++ {
		// 2.
		odd := helper(s, i, i)
		// 3.
		if len(odd) > len(result) {
			result = odd
		}
		// 4.
		even := helper(s, i, i+1)
		// 5.
		if len(even) > len(result) {
			result = even
		}
	}

	// 6.
	return result
}

func helper(s string, l, r int) string {
	// 0.
	for l >= 0 && r < len(s) && s[l] == s[r] {
		// 1.
		l--
		r++
	}

	// 2.
	return string(s[l+1 : r])
}
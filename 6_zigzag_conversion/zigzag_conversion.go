import "strings"

func convert(s string, numRows int) string {
	// 0.
	if numRows <= 1 {
		return s
	}

	// 1.
	lines := make([]string, numRows)
	index := 0
	step := 1

	// 2.
	for i := 0; i < len(s); i++ {
		// 3.
		lines[index] = lines[index] + string(s[i])
		// 4.
		index = index + step
		// 5.
		if index == 0 || index == numRows-1 {
			step = step * -1
		}
	}

	// 6.
	return strings.Join(lines[:], "")
}



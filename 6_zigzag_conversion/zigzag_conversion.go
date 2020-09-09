import "strings"

func convert(s string, numRows int) string {
	// 0.
	if numRows <= 1 {
		return s
	}

	// 1.
	lines := make([]string, numRows)
	row := 0
	step := 1

	// 2.
	for i := 0; i < len(s); i++ {
		// 3.
		lines[row] = lines[row] + string(s[i])

		// 4.
		if row == 0 || row == numRows-1 {
			step = step * -1
		}

		// 5.
		row = row + step
	}

	// 6.
	return strings.Join(lines[:], "")
}



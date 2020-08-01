

// Approach 2: Iterative
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	// 0.
	cur := &ListNode{}
	dummy := cur
	c := 0

	// 1.
	for l1 != nil || l2 != nil || c != 0 {

		// 2.
		if l1 != nil {
			c += l1.Val
			l1 = l1.Next
		}

		// 3.
		if l2 != nil {
			c += l2.Val
			l2 = l2.Next
		}

		// 4.
		cur.Next = &ListNode{Val: c % 10}
		// 5.
		cur = cur.Next
		// 6.
		c = c / 10

	}

	// 7.
	return dummy.Next
}
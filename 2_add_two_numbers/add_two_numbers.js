// Approach 1: Recursive
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @param {int} c
 * @return {ListNode}
 */
function addTwoNumbers(l1, l2, c = 0) {
  // 0.
  if (!l1 && !l2 && !c) return null;
  // 1.
  const sum = c + (l1 && l1.val) + (l2 && l2.val);
  // 2.
  c = Math.trunc(sum / 10);
  // 3.
  const node = new ListNode(sum % 10);
  // 4-7.
  node.next = addTwoNumbers(l1 && l1.next, l2 && l2.next, c);
  // 8.
  return node;
}

// Approach 2: Iterative
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

function addTwoNumbers(l1, l2) {
  // 0.
  var dummy = (cur = new ListNode(0));
  var c = 0;

  // 1.
  while (l1 || l2 || c) {
    // 2.
    if (l1) {
      c += l1.val;
      l1 = l1.next;
    }

    // 3.
    if (l2) {
      c += l2.val;
      l2 = l2.next;
    }

    // 4.
    cur.next = new ListNode(c % 10);
    // 5.
    cur = cur.next;
    // 6.
    c = Math.trunc(c / 10);
  }

  // 7.
  return dummy.next;
}

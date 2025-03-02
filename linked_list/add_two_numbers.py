from typing import Optional

from linked_list.merge_two_sorted_list import print_linked_list, create_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = node = ListNode()

    rev_l1 = reverse(l1)
    rev_l2 = reverse(l2)

    carry_over = 0
    while rev_l1 or rev_l2 or carry_over:
        val1 = rev_l1.val if rev_l1 else 0
        val2 = rev_l2.val if rev_l2 else 0

        addition = val1 + val2 + carry_over
        left_over = addition % 10
        carry_over = addition // 10

        node.next = ListNode(left_over)
        node = node.next

        rev_l1 = rev_l1.next if rev_l1 else None
        rev_l2 = rev_l2.next if rev_l2 else None

    return dummy.next


def reverse(l: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, l
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


if __name__ == '__main__':
    l1 = create_linked_list([1, 2, 9])
    l2 = create_linked_list([4, 5, 6])

    print("List 1:")
    print_linked_list(l1)
    print("List 2:")
    print_linked_list(l2)

    result = addTwoNumbers(l1, l2)
    print("Resultant List:")
    print_linked_list(result)

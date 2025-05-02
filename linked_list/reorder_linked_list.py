from typing import Optional

from linked_list.utils import print_linked_list, create_linked_list, ListNode


def reorderList(head: Optional[ListNode]) -> None:
    if not head or not head.next:
        return

    # Step 1: Find the middle of the list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev, curr = None, slow.next
    slow.next = None  # Split the list into two halves
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    # Step 3: Merge the two halves
    first, second = head, prev

    print_linked_list(first)
    print_linked_list(second)
    while second:
        first_next, second_next = first.next, second.next
        first.next = second
        second.next = first_next
        first, second = first_next, second_next
    print_linked_list(head)




if __name__ == '__main__':
    l1 = create_linked_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print(reorderList(l1))

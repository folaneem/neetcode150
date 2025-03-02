from binascii import b2a_hex
from typing import Optional

from linked_list.linked_list_cycle import ListNode
from linked_list.merge_two_sorted_list import print_linked_list, create_linked_list


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head
    behind = ahead = dummy
    for _ in range(n + 1):
        ahead = ahead.next

    while ahead:
        behind = behind.next
        ahead = ahead.next
    print_linked_list(behind)
    behind.next = behind.next.next
    print_linked_list(ahead)
    print_linked_list(behind)
    print_linked_list(dummy.next)
    print_linked_list(head)



if __name__ == '__main__':
    l1 = create_linked_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print(removeNthFromEnd(head=l1, n=4))

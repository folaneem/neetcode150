from typing import Optional

from linked_list.merge_two_sorted_list import create_linked_list, print_linked_list, ListNode


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    groupPrev = dummy

    while True:
        print("Group Prev")
        print_linked_list(groupPrev)
        kth = getKth(groupPrev, k)
        if not kth:
            break
        print("Kth")
        print_linked_list(kth)
        groupNext = kth.next
        prev, curr = kth.next, groupPrev.next
        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    return dummy.next


def getKth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr


# Example usage
if __name__ == "__main__":
    l = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 5, 3, 2])
    k = 4
    print("Original List:")
    print_linked_list(l)

    result = reverseKGroup(l, k)
    print("Reversed in k-groups:")
    print_linked_list(result)

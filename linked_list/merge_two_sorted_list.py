from linked_list.utils import ListNode, create_linked_list, print_linked_list


def merge_sorted_linked_lists(l1, l2):
    # Create a dummy node to simplify handling of the new list
    dummy = ListNode()
    current = dummy

    # Traverse both lists
    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach the remaining part of l1 or l2
    if l1:
        current.next = l1
    elif l2:
        current.next = l2

    return dummy.next


if __name__ == '__main__':
    # Example usage
    l1 = create_linked_list([1, 3, 5, 7])
    l2 = create_linked_list([2, 4, 6, 8])

    print_linked_list(l1)
    print_linked_list(l2)

    merged = merge_sorted_linked_lists(l1, l2)
    print_linked_list(merged)

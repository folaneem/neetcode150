class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

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


# Helper functions to create and print linked lists
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def print_linked_list(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    print(" -> ".join(map(str, values)))


if __name__ == '__main__':
    # Example usage
    l1 = create_linked_list([1, 3, 5, 7])
    l2 = create_linked_list([2, 4, 6, 8])

    print_linked_list(l1)
    print_linked_list(l2)

    merged = merge_sorted_linked_lists(l1, l2)
    print_linked_list(merged)

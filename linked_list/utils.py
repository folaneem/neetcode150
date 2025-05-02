class ListNode:
    def __init__(self, value=0, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

    def __str__(self):
        return str(self.value)


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

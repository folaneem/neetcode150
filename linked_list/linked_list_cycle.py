# Floyed Tortoise and Hare (Slow and Fast Pointers)
from typing import Optional

from linked_list.utils import ListNode


def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True

    return False

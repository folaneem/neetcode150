from linked_list.utils import ListNode


def reverseList(head):
    prev, curr = None, head

    while curr:
        next = curr.next
        curr.next = prev
        curr = next
        prev = curr
    return prev


three = ListNode(value=3, next=None)
two = ListNode(value=2, next=three)
one = ListNode(value=1, next=two)
zero = ListNode(value=0, next=one)

result = reverseList(head=zero)
print()
# NULL -> 0 -> 1 -> 2 -> 3 -> NULL
# NULL <- 0 <- 1 <- 2 <- 3 <- NULL
# 0, curr = 0 prev = null next = 1
# 1, curr = 1 prev = 0 next = 2
# 0, curr = 0, prev = 1 next null
# 1, curr = 1, prev =2 next 1
#

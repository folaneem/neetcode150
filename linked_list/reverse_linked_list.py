class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev, curr = None, head

    while curr:
        next = curr.next
        curr.next = prev
        curr = next
        prev = curr
    return prev

three = ListNode(val=3, next=None)
two = ListNode(val=2, next=three)
one = ListNode(val=1, next=two)
zero = ListNode(val=0, next=one)

result = reverseList(head=zero)
print()
# NULL -> 0 -> 1 -> 2 -> 3 -> NULL
# NULL <- 0 <- 1 <- 2 <- 3 <- NULL
# 0, curr = 0 prev = null next = 1
# 1, curr = 1 prev = 0 next = 2
# 0, curr = 0, prev = 1 next null
# 1, curr = 1, prev =2 next 1
#

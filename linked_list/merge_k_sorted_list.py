from linked_list.reverse_linked_list import ListNode


def merge_k_sorted_list(lists):
    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = None
            if i + 1 < len(lists):
                l2 = lists[i + 1]
            mergedLists.append(merge(l1, l2))
        lists = mergedLists
    return lists[0]

def merge(l1: ListNode, l2: ListNode):
    dummy = node = ListNode()

    while l2 and l1:
        if l2.val > l1.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next
    if l2:
        node.next = l2
    if l1:
        node.next = l1
    return dummy.next


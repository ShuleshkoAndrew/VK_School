def hasCycle(head) -> bool:
    if head is None or head.next is None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if fast == None or fast.next == None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


def reverseLinkedList(head):
    prev = None
    current = head

    while (current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next

    head = prev
    return head

none a b c d none

prev = none
current <- a
next <-
current.next <- b
prev <- a
current = a

def middleNode() -> Node:
    slow, fast = head, head
    while(fast not is None and fast.next not is None):
        slow = slow.next
        fast = fast.next.next
    return slow

class ListNode:
    def init(self):
        self.val = val

    def RemoveElements(head, val):

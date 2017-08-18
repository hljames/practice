from linkedlists import linkedlists

def duplicates (ll):
    if ll.head is None:
        return ll
    current = ll.head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next
    return ll

def follow_up(ll):
    if ll.head is None:
        return
    slow = ll.head
    while slow:
        fast = slow
        while fast.next:
            if fast.next.value = slow.value:
                fast.next = fast.next.next
            else:
                fast = fast.next
        slow = slow.next
    return ll

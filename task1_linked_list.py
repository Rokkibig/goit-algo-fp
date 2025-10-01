class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        res = []
        current = self.head
        while current:
            res.append(current.data)
            current = current.next
        return res

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def merge_sorted(self, other):
        dummy = Node(0)
        tail = dummy
        a, b = self.head, other.head
        while a and b:
            if a.data < b.data:
                tail.next, a = a, a.next
            else:
                tail.next, b = b, b.next
            tail = tail.next
        tail.next = a or b
        merged = LinkedList()
        merged.head = dummy.next
        return merged

    def sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if not head or not head.next:
            return head
        mid = self._get_middle(head)
        right = mid.next
        mid.next = None
        left_sorted = self._merge_sort(head)
        right_sorted = self._merge_sort(right)
        return self._merge(left_sorted, right_sorted)

    def _get_middle(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, a, b):
        dummy = Node(0)
        tail = dummy
        while a and b:
            if a.data < b.data:
                tail.next, a = a, a.next
            else:
                tail.next, b = b, b.next
            tail = tail.next
        tail.next = a or b
        return dummy.next

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


def search_key(head, key):
    current = head
    while current is not None:
        if current.data == key:
            return True
        current = current.next
    return False


if __name__ == '__main__':
    head = Node(12)
    head.next = Node(22)
    head.next.next = Node(33)
    head.next.next.next = Node(44)
    head.next.next.next.next = Node(55)
    head.next.next.next.next.next = Node(66)

    key = 22

    if search_key(head, key):
        print("Found")
    else:
        print("Not Found")

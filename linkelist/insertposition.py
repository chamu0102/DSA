class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def insert_pos(head, pos, data):
    new_node = Node(data)

    # Insert at the front
    if pos == 1:
        new_node.next = head
        return new_node

    current = head

    # Traverse to the (pos - 1)th node
    for _ in range(1, pos - 1):
        if current is None:
            return head  # Position is beyond length
        current = current.next

    # Insert after current
    if current is None:
        return head  # Again, position is too far

    new_node.next = current.next
    current.next = new_node

    return head


def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    data = 12
    pos = 3
    head = insert_pos(head, pos, data)

    print("List after inserting 12 at position 3:")
    print_list(head)


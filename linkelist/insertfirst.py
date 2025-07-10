class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def insert_at_front(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    return new_node

def print_list(head):
    current = head
    while current is not None:
        print(f"{current.data}", end=" ")
        current = current.next
    print()

if __name__ == '__main__':
    head = Node(4)
    head.next = Node(6)
    head.next.next = Node(3)
    head.next.next.next = Node(23)

    print("Original linked list:", end=" ")
    print_list(head)

    print("After inserting at front:", end=" ")
    data = 1
    head = insert_at_front(head, data)
    print_list(head)





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def append(head, new_data):
    new_node = Node(new_data)
    if head is None:
        return new_node

    last = head
    while last.next:
        last = last.next

    last.next = new_node
    return head

def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

if __name__ == '__main__':
    head = Node(11)
    head.next = Node(22)
    head.next.next = Node(33)
    head.next.next.next = Node(44)
    head.next.next.next.next = Node(55)

    print("Created linked list is:", end=" ")
    print_list(head)

    head = append(head, 66)

    print("After append:", end=" ")
    print_list(head)


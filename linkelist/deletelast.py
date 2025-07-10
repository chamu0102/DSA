class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_last_node(head):
    if not head:
        return None
    if not head.next:
        return None  # Only one node, so remove it

    second_last = head
    while second_last.next.next:
        second_last = second_last.next

    second_last.next = None
    return head

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Original list:")
    print_list(head)

    head = remove_last_node(head)

    print("List after removing the last node:")
    print_list(head)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_head(head):
    if head is None:
        return None

    temp = head
    head = head.next

    del temp
    return head

def print_list(current):
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

if __name__ == '__main__':
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

    head = delete_head(head)

    print("After deleting head node:")
    print_list(head)

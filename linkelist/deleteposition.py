class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteNode(head, position):
    temp = head

    if temp is None:
        return head

    # Deleting head node
    if position == 1:
        return temp.next

    # Traverse to the node before the one to delete
    for i in range(1, position - 1):
        if temp is None or temp.next is None:
            print("Position out of range")
            return head
        temp = temp.next

    # If the node to delete is valid
    if temp.next is not None:
        temp.next = temp.next.next
    else:
        print("Position out of range")

    return head

def printList(head):
    while head:
        print(f"{head.data}->", end=" ")
        head = head.next
    print("None")

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original list: ", end="")
    printList(head)

    position = 2
    head = deleteNode(head, position)

    print("List after deletion: ", end="")
    printList(head)


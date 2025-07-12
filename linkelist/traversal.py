class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def traverseList(current):
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

def main():
    current = Node(9)
    current.next = Node(22)
    current.next.next = Node(35)
    current.next.next.next = Node(42)
    current.next.next.next.next = Node(47)

    traverseList(current)

if __name__ == "__main__":
    main()

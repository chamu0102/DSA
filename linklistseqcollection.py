class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  # head node of the list


    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


    def insert_at_position(self, position, data):
        if position < 0:
            print("Position must be >= 0")
            return

        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        for i in range(position - 1):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next

        new_node.next = current.next
        current.next = new_node


    def delete_by_value(self, key):
        current = self.head

        if current is not None and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print("Key not found")
            return

        prev.next = current.next


    def delete_by_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            return

        for i in range(position - 1):
            temp = temp.next
            if temp is None or temp.next is None:
                print("Position out of bounds")
                return

        temp.next = temp.next.next


    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False


    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)
    ll.insert_at_position(1, 7)

    print("Linked List:")
    ll.display()

    print("Length:", ll.get_length())

    print("Search 7:", ll.search(7))
    print("Search 100:", ll.search(100))

    ll.delete_by_value(7)
    ll.delete_by_position(2)

    print("After Deletion:")
    ll.display()

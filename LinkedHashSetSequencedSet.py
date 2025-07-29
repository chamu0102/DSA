class LinkedHashSetSequencedSet:
    def __init__(self):
        self.data = dict()  

    def add(self, value):
        if value not in self.data:
            self.data[value] = len(self.data)

    def remove(self, value):
        if value in self.data:
            del self.data[value]
            self.data = {k: i for i, k in enumerate(self.data)}

    def contains(self, value):
        return value in self.data

    def get(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return list(self.data.keys())[index]

    def index_of(self, value):
        if value in self.data:
            return list(self.data.keys()).index(value)
        return -1

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def clear(self):
        self.data.clear()

    def __iter__(self):
        return iter(self.data.keys())

    def __str__(self):
        return "[" + ", ".join(str(k) for k in self.data.keys()) + "]"
setx = LinkedHashSetSequencedSet()
setx.add(100)
setx.add(200)
setx.add(300)
setx.add(200)

print("Set contents:", setx)
print("Contains 200?", setx.contains(200))
print("Contains 400?", setx.contains(400))

print("Element at index 1:", setx.get(1))

print("Index of 300:", setx.index_of(300))

setx.remove(200)
print("After removing 200:", setx)

print("Size:", setx.size())
print("Is empty?", setx.is_empty())

setx.clear()
print("Cleared set:", setx)

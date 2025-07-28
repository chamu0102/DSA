class HashSet:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def add(self, key):
        index = self._hash_function(key)
        if key not in self.table[index]:
            self.table[index].append(key)
            print(f"{key} added to set.")
        else:
            print(f"{key} already exists in set.")

    def remove(self, key):
        index = self._hash_function(key)
        if key in self.table[index]:
            self.table[index].remove(key)
            print(f"{key} removed from set.")
        else:
            print(f"{key} not found in set.")

    def contains(self, key):
        index = self._hash_function(key)
        return key in self.table[index]

    def display(self):
        print("Hash Set Contents:")
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")
if __name__ == "__main__":
    hs = HashSet()

    hs.add(10)
    hs.add(20)
    hs.add(15)
    hs.add(25)
    hs.add(10) 

    hs.display()

    print("Contains 15?", hs.contains(15))
    print("Contains 100?", hs.contains(100))

    hs.remove(20)
    hs.remove(99)  # not in set

    hs.display()

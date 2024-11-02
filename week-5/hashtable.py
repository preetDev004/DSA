
# Chaining method

class HashTable:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.num_elements = 0
        self.table = [[] for _ in range(self.capacity)]

    def hash_function(self, key):
        return hash(key) % self.capacity 
    
    def calc_load_factor(self):
        return self.num_elements / self.capacity
    
    def insert(self, key, value):

        if self.calc_load_factor() > 0.7:
            self.resize()

        index = self.hash_function(key)
        
        if len(self.table[index]) > 0:
            for k, _ in self.table[index]:
                if k == key:
                    print("Key already exists, Cannot insert!")
                    return
        self.table[index].append((key,value))
        self.num_elements += 1

    def resize(self):
        old_table = self.table
        self.num_elements = 0
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]

        for bucket in old_table:
            for k, v in bucket:
                self.insert(k, v)

    def display(self):
            print("\n" + "=" * 50)
            print(f"Hash Table (Capacity: {self.capacity}, Elements: {self.num_elements})")
            print("=" * 50)
            
            for i, bucket in enumerate(self.table):
                print(f"\nBucket {i}:")
                if not bucket:
                    print("  <empty>")
                else:
                    for k, v in bucket:
                        print(f"  Key: {k:<15} Value: {v}")
            
            print("\n" + "=" * 50)
            print(f"Load Factor: {self.calc_load_factor():.2f}")
            print("=" * 50 + "\n")


if __name__ == "__main__":
    table = HashTable()
    table.insert("preet", 94)
    table.insert("madhav", 86)
    table.insert("Jivin", 72)
    table.insert("Amitoj", 72)
    print(f"Load factor (λ): {table.calc_load_factor()}")
    table.insert("Nand", 76)
    table.insert("Sean", 75)
    table.insert("Cris", 75)
    table.insert("Vlad", 100)
    print(f"Load factor (λ): {table.calc_load_factor()}")
    table.insert("Maksym", 99)
    table.insert("preet", 94)
    table.insert("Samay Raina", 999)
    table.insert("Karan Aujla", 99999)
    table.insert("Diljit", 9999)
    print(f"Load factor (λ): {table.calc_load_factor()}")

    table.display()
#    Main Author(s): Preet Dineshkumar Patel, Madhav Rajpal
#    Main Reviewer(s): Sukhman Hara

class HashTable:
    
	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice as long as it is a hash table
    
    def __init__(self, capacity=32):
        # Initialize the hash table with a given capacity
        # Default capacity is 32
        self.table = [None] * capacity
        self.size = 0
        self.TOMBSTONE = "TOMBSTONE"

    def insert(self, key, value):
        # Insert a key-value pair into the hash table
        # Returns True if insertion is successful, False if key already exists
        initial_position = hash(key) % len(self.table)
        position = initial_position
        first_tombstone_position = -1
        
        while True:
            if self.table[position] is None:
                break
            elif self.table[position] == self.TOMBSTONE:
                if first_tombstone_position == -1:
                    first_tombstone_position = position
            elif self.table[position][0] == key:
                return False
            position = (position + 1) % len(self.table)
            if position == initial_position:
                break
        
        # Resize the table if load factor exceeds 0.7
        if (self.size + 1) / len(self.table) >= 0.7:
            self._resize()
            initial_position = hash(key) % len(self.table)
            position = initial_position
            first_tombstone_position = -1
            while self.table[position] is not None and self.table[position] != self.TOMBSTONE:
                position = (position + 1) % len(self.table)
        
        final_position = first_tombstone_position if first_tombstone_position != -1 else position
        self.table[final_position] = (key, value)
        self.size += 1
        return True

    def modify(self, key, value):
        # Modify the value associated with a given key
        # Returns True if modification is successful, False if key is not found
        initial_position = hash(key) % len(self.table)
        position = initial_position
        
        while True:
            if self.table[position] is None:
                return False
            elif self.table[position] != self.TOMBSTONE and self.table[position][0] == key:
                self.table[position] = (key, value)
                return True
            position = (position + 1) % len(self.table)
            if position == initial_position:
                return False

    def remove(self, key):
        # Remove a key-value pair from the hash table
        # Returns True if removal is successful, False if key is not found
        initial_position = hash(key) % len(self.table)
        position = initial_position
        
        while True:
            if self.table[position] is None:
                return False
            elif self.table[position] != self.TOMBSTONE and self.table[position][0] == key:
                self.table[position] = self.TOMBSTONE
                self.size -= 1
                return True
            position = (position + 1) % len(self.table)
            if position == initial_position:
                return False

    def search(self, key):
        # Search for a value associated with a given key
        # Returns the value if found, None otherwise
        initial_position = hash(key) % len(self.table)
        position = initial_position
        
        while True:
            if self.table[position] is None:
                return None
            elif self.table[position] != self.TOMBSTONE and self.table[position][0] == key:
                return self.table[position][1]
            position = (position + 1) % len(self.table)
            if position == initial_position:
                return None

    def capacity(self):
        # Return the current capacity of the hash table
        return len(self.table)

    def __len__(self):
        # Return the number of key-value pairs in the hash table
        return self.size

    def _resize(self):
        # Helper method to resize the hash table when load factor exceeds 0.7
        old_table = self.table
        self.table = [None] * (len(old_table) * 2)
        self.size = 0
        
        for item in old_table:
            if item and item != self.TOMBSTONE:
                self.insert(item[0], item[1])
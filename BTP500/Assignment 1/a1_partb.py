#    Main Author(s): Preet Dineshkumar Patel
#    Main Reviewer(s): Madhav Rajpal, Sukhman Hara




class SortedList:
    class Node:
        def __init__(self, data, next = None, prev = None):
            # Initialize a node with data and optional next and prev pointers
            self.data = data
            self.next = next
            self.prev = prev

        def get_data(self):
            # Return the data stored in the node
            return self.data

        def get_next(self):
            # Return the next node in the list
            return self.next

        def get_previous(self):
            # Return the previous node in the list
            return self.prev

    def __init__(self):
        # Initialize an empty sorted list
        self.front = None
        self.back = None
        self.size = 0

    def get_front(self):
        # Return the front node of the list
        return self.front

    def get_back(self):
        # Return the back node of the list
        return self.back

    def is_empty(self):
        # Check if the list is empty
        return self.size == 0

    def __len__(self):
        # Return the size of the list
        return self.size

    def insert(self, data):
        # Insert a new node with the given data in the correct position to maintain sorted order
        # Returns the newly inserted node or raises ValueError if data is None
        if data is not None:
            new_node = self.Node(data)
            self.size += 1
            if self.front is None and self.back is None:
                self.front = new_node
                self.back = new_node
                return new_node
            
            if data <= self.front.get_data():
                new_node.next = self.front
                self.front.prev = new_node
                self.front = new_node
                return new_node

            if data >= self.back.get_data():
                new_node.prev = self.back
                self.back.next = new_node
                self.back = new_node
                return new_node
            
            current = self.front
            while current and data >= current.get_data():
                current = current.get_next()

            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node

            return new_node
        raise ValueError('Cannot insert data referred to by None')

    def erase(self, node):
        # Remove the specified node from the list
        # Raises ValueError if node is None
        if node is not None:
            self.size -= 1
            if self.front == node and self.back == node:
                self.front = None
                self.back = None 
                return
            
            if self.front == node:
                self.front = self.front.get_next()
                self.front.prev = None
                return
            
            if self.back == node:
                self.back = self.back.get_previous()
                self.back.next = None
                return
            
            node.next.prev = node.prev
            node.prev.next = node.next
            return

        raise ValueError('Cannot erase node referred to by None')

    def search(self, data):
        # Search for a node with the given data
        # Returns the node if found, None if not found, or raises ValueError if data is None
        if data is not None:
            if data == self.back.get_data():
                return self.back
            
            current = self.front
            while current:
                if data == current.get_data():
                    return current
                if data < current.get_data(): 
                    return None
                current = current.get_next()
            return None

        raise ValueError('Cannot search data referred to by None')
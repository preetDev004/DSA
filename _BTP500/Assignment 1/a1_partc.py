#    Main Author(s): Madhav Rajpal
#    Main Reviewer(s): Sukhman Hara, Preet Dineshkumar Patel



class Stack:

	def __init__(self, cap = 10):
		self.items = [None] * cap
		self.size = 0

	def capacity(self):
		return len(self.items)

	def push(self, data):
		# self.items.append(data)
		if self.size + 1 >= self.capacity():
			new_items = [None] * (self.capacity() * 2)
			for i in range(self.size):
				new_items[i] = self.items[i]
			self.items = new_items
		self.items[self.size] = data
		self.size += 1

	def pop(self):
		if self.is_empty():
			raise IndexError("pop() used on empty stack")
		self.size -= 1
		return self.items[self.size]

	def get_top(self):
		if self.is_empty():
			return None
		return self.items[self.size-1]

	def is_empty(self):
		return self.size == 0

	def __len__(self):
		return self.size


class Queue:


	def __init__(self, cap = 10):
		self.items = [None] * cap
		self.size = 0
		self.front = 0

	def capacity(self):
		return len(self.items)

	def enqueue(self, data):
		# self.items.append(data)
		if self.size + 1 > self.capacity():
			new_items = [None] * (self.capacity() * 2)
			for i in range(self.size):
				new_items[i] = self.items[(self.front + i) % self.capacity()]
			self.items = new_items
			self.front = 0
		self.items[(self.size + self.front) % self.capacity()] = data
		self.size += 1

	def dequeue(self):		
		if self.is_empty():
			raise IndexError("dequeue() used on empty queue")
		poped = self.items[self.front]
		self.front = (self.front+1) % self.capacity()
		self.size -= 1
		return poped

	def get_front(self):
		if self.is_empty():
			return None
		return self.items[self.front]

	def is_empty(self):
		return self.size == 0

	def __len__(self):
		return self.size


class Deque:
    def __init__(self, cap=10):
        self._data = [None] * cap
        self._capacity = cap
        self._size = 0
        self._front = 0
        
    def capacity(self):
        return self._capacity
        
    def _resize(self):
        new_data = [None] * (self._capacity * 2)
        for i in range(self._size):
            new_data[i] = self._data[(self._front + i) % self._capacity]
        self._data = new_data
        self._capacity *= 2
        self._front = 0
        
    def push_front(self, data):
        if self._size == self._capacity:
            self._resize()
            
        self._front = (self._front - 1) % self._capacity
        self._data[self._front] = data
        self._size += 1
        
    def pop_front(self):
        if self.is_empty():
            raise IndexError('pop_front() used on empty deque')
            
        value = self._data[self._front]
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return value
        
    def push_back(self, data):
        if self._size == self._capacity:
            self._resize()
            
        back = (self._front + self._size) % self._capacity
        self._data[back] = data
        self._size += 1
        
    def pop_back(self):
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')
            
        back = (self._front + self._size - 1) % self._capacity
        value = self._data[back]
        self._size -= 1
        return value
        
    def get_front(self):
        if self.is_empty():
            return None
        return self._data[self._front]
        
    def get_back(self):
        if self.is_empty():
            return None
        back = (self._front + self._size - 1) % self._capacity
        return self._data[back]
        
    def is_empty(self):
        return self._size == 0
        
    def __len__(self):
        return self._size
        
    def __getitem__(self, k):
        if k < 0 or k >= self._size:
            raise IndexError('Index out of range')
        return self._data[(self._front + k) % self._capacity]

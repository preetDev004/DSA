class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
        parent = (index - 1) // 2

        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def remove(self):
        if not self.heap:
            return None

        max_ele = self.heap[0]
        last_ele = self.heap.pop()

        if self.heap:
            self.heap[0] = last_ele
            self._bubble_down(0)

        return max_ele

    def _bubble_down(self, index):
        length = len(self.heap)

        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            largest = index

            if left_child < length and self.heap[index] < self.heap[left_child]:
                largest = left_child

            if right_child < length and self.heap[index] < self.heap[right_child]:
                largest = right_child

            if largest == index:
                break

            self.heap[largest], self.heap[index] =  self.heap[index], self.heap[largest],
            index = largest

    def peek(self):
        if not self.heap:
            return
        return self.heap[0]

    def __str__(self):
        return str(self.heap)


if __name__ == "__main__":
    heap = BinaryHeap()
    heap.insert(10)
    heap.insert(20)
    heap.insert(5)
    heap.insert(30)
    heap.insert(15)

    print("Heap:", heap)
    print("Max value:", heap.peek())
    print("Removing max:", heap.remove())
    print("Heap after removal:", heap)

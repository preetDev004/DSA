import sys
import os

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the lab3 directory
lab3_dir = os.path.join(current_dir, '..', 'Labs', 'lab3')

# Add the lab3 directory to the Python path
sys.path.append(os.path.abspath(lab3_dir))

# Try to import the module
try:
    import lab3 as l3
    print("Successfully imported lab3")
except ImportError as e:
    print(f"Failed to import lab3: {e}")
    print(f"Current sys.path: {sys.path}")

class QueueLinkedList:
    def __init__(self):
        self.list = l3.LinkedList()
    
    def enqueue(self,data):
        self.list.push_back(data)
    
    def dequeue(self):
        return self.list.pop_front()
    
class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self,data):
        self.list.append(data)
    
    def dequeue(self):
        if len(self.list) == 0:
            return None
        return self.list.pop(0)


if __name__ == "__main__":
    my_ll_queue = QueueLinkedList()
    my_ll_queue.dequeue()

    my_ll_queue.enqueue(12)
    my_ll_queue.enqueue(2)
    my_ll_queue.enqueue(112)
    my_ll_queue.enqueue(13)
    my_ll_queue.enqueue(103)
    my_ll_queue.dequeue()

    for item in my_ll_queue.list:
        print(item)

    print()
    my_queue = QueueLinkedList()
    my_queue.dequeue()
    my_queue.enqueue(12)
    my_queue.enqueue(2)
    my_queue.enqueue(112)
    my_queue.enqueue(13)
    my_queue.enqueue(103)
    my_queue.dequeue()
    for item in my_queue.list:
        print(item)

    print()
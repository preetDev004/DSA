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

class StackLinkedList:
    def __init__(self):
        self.list = l3.LinkedList()
    
    def push(self,data):
        self.list.push_back(data)
    
    def pop(self):
        return self.list.pop_back()
    
class Stack:
    def __init__(self):
        self.list = []

    def push(self,data):
        self.list.append(data)
    
    def pop(self):
        return self.list.pop()


if __name__ == "__main__":
    my_ll_stack = StackLinkedList()
    my_ll_stack.pop()

    my_ll_stack.push(12)
    my_ll_stack.push(2)
    my_ll_stack.push(112)
    my_ll_stack.push(13)
    my_ll_stack.push(103)
    my_ll_stack.pop()

    for item in my_ll_stack.list:
        print(item)

    print()
    my_stack = StackLinkedList()
    my_stack.pop()
    my_stack.push(12)
    my_stack.push(2)
    my_stack.push(112)
    my_stack.push(13)
    my_stack.push(103)
    my_stack.pop()
    for item in my_stack.list:
        print(item)

    print()
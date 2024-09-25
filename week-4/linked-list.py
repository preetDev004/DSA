class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SentinelNode:
    def __init__(self):
        self.next = None

# Simple Linked List
class Linkedlist:
    def __init__(self):
        self.sentinel = SentinelNode()
        self.size = 0
    
    def pushBack(self, data):
        """ Append the node at the end """
        new_node = Node(data)
        last = self.sentinel

        while last.next:
            last = last.next
        
        last.next = new_node
        self.size += 1

    def pushFirst(self, data):
        """adds new element at the beginning """
        new_node = Node(data)
        new_node.next = self.sentinel.next
        self.sentinel.next = new_node
        self.size += 1

    def popBack(self):
        """Pops the last element"""
        if not self.sentinel.next:
            return None
        last = self.sentinel
        while last.next.next:
            last = last.next
        poped_element = last.next.data
        last.next = None
        self.size -= 1
        return poped_element
    
    def popFirst(self):
        """Pops first element"""
        if not self.sentinel.next:
            return None
        poped_elem = self.sentinel.next.data
        self.sentinel.next = self.sentinel.next.next
        self.size -= 1
        return poped_elem
  
    def display(self):
        print("size of the linked-list: ", self.size)
        elem = self.sentinel
        while elem.next:
            print(elem.next.data)
            elem = elem.next
    
l1 = Linkedlist()
l1.pushBack(23)
l1.pushBack(320)
l1.pushBack(53)
l1.pushFirst(550)
l1.pushFirst(20)
l1.display()
poped = l1.popBack()
print("The poped item is: ",poped )
popedF = l1.popFirst()
print("The poped item is: ",popedF )
l1.display()
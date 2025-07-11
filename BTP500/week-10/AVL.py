import queue
'''
Augumenting last week's BST such that it will be height balanced,
thus becoming an AVL tree.

A tree is height balanced if for every node within the
tree, the height of its right and left subtrees differ by no
more than one.

In the case of the AVL tree, the balance of a node is calculated:

Node's balance = height of right - height of left
     of node        subtree          subtree
'''

class AVL_Tree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.balance = 0    # Use to check the balance factor...

    def reBalance_helper(self):
        """Helper function to handle re-balancing of the tree"""
        if self.balance < -1:  # Left-heavy :- Need to rotate right.
            if self.left and self.left.balance > 0:  # Left-Right case :- left child is right heavy
                self.left = self.left.left_rotate()
            return self.right_rotate()  # Rotate right
        elif self.balance > 1:  # Right-heavy :- need to rotate left.
            if self.right and self.right.balance < 0:  # Right-Left case :- right child is left heavy
                self.right = self.right.right_rotate()
            return self.left_rotate()   # Rotate Left
        return self

    def left_rotate(self):
        """Fixed left rotation implementation"""
        if not self.right:  # if there is no right child, rotation not possible
            return self

        new_root = self.right  # The new root of the subtree will be the right child
        self.right = new_root.left  # The left child of the new root becomes the right child of the old root
        new_root.left = self  # The current node becomes the left child of the new root

        # Update balance factors, after each rotation
        self.balance = self.find_balance()
        new_root.balance = new_root.find_balance()

        return new_root

    def right_rotate(self):
        """Fixed right rotation implementation"""
        if not self.left:  # If there is no left child, rotation is not possible
            return self

        new_root = self.left  # The new root of the subtree will be the left child
        self.left = new_root.right  # The right child of the new root becomes the left child of the old root
        new_root.right = self  # The current node becomes the right child of the new root

        # Update balance factors after each rotation
        self.balance = self.find_balance()
        new_root.balance = new_root.find_balance()

        return new_root

    def insert(self, data):
        """Fixed insert implementation with proper balancing"""
        if not self.data:  # If the current node is empty
            self.data = data
            return self

        # Insert the data into the left or right subtree depending on its value
        if data < self.data:
            if not self.left:
                self.left = AVL_Tree(data)
            else:
                self.left = self.left.insert(data)
        elif data > self.data:
            if not self.right:
                self.right = AVL_Tree(data)
            else:
                self.right = self.right.insert(data)

        # Update balance factor
        self.balance = self.find_balance()

        # Re-balance if necessary (the balance factor exceeds the limit)
        if abs(self.balance) > 1:
            return self.reBalance_helper()

        return self

    def find_balance(self):
        """Calculate balance factor correctly"""
        right_height = self.right.find_height() if self.right else 0
        left_height = self.left.find_height() if self.left else 0
        return right_height - left_height

    def find_height(self):
        """Correctly calculate height"""
        if not self.data:
            return 0

        left_height = self.left.find_height() if self.left else 0
        right_height = self.right.find_height() if self.right else 0
        return 1 + max(left_height, right_height)

    def min_value_node(self):
        """Find minimum value node"""
        current = self
        while current.left:
            current = current.left
        return current

    def delete(self, data):
        """Fixed delete implementation with proper re-balancing"""
        if not self.data:
            return self

        if data < self.data:   # If the data is smaller than the current node, delete from the left subtree
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:  # If the data is larger than the current node, delete from the right subtree
            if self.right:
                self.right = self.right.delete(data)
        else:
            # Node with one child or no child
            if not self.left:
                return self.right
            elif not self.right:
                return self.left

            # Node with two children
            temp = self.right.min_value_node()   # Find the inorder successor (min value node in right subtree)
            self.data = temp.data   # Replace the current node's data with the inorder successor's data
            self.right = self.right.delete(temp.data)   # Delete the inorder successor from the right subtree

        # Update balance
        self.balance = self.find_balance()

        # Re-balance if necessary
        if abs(self.balance) > 1:
            return self.reBalance_helper()

        return self

    def search(self, data):
        """Search implementation remains the same"""
        if not self.data:
            return False

        if self.data == data:
            return True
        elif data < self.data and self.left:
            return self.left.search(data)
        elif data > self.data and self.right:
            return self.right.search(data)
        return False

    # Your existing printing methods remain unchanged
    def inorder_print(self):
        if self.data:
            if self.left:
                self.left.inorder_print()
            print(self.data, end=" ")
            if self.right:
                self.right.inorder_print()

    def pre_order_print(self):
        if self.data:
            print(self.data, end=" ")
            if self.left:
                self.left.pre_order_print()
            if self.right:
                self.right.pre_order_print()

    def post_order_print(self):
        if self.data:
            if self.left:
                self.left.post_order_print()
            if self.right:
                self.right.post_order_print()
            print(self.data, end=" ")

    def breadth_first_print(self):
        the_nodes = queue.Queue()
        if self.data:
            the_nodes.put(self)
        while not the_nodes.empty():
            curr = the_nodes.get()
            if curr.left:
                the_nodes.put(curr.left)
            if curr.right:
                the_nodes.put(curr.right)
            print(curr.data, end=" ")

    def print_tree(self, prefix="", is_left=False):
        if self.data:
            print(prefix, end="")
            print("|__" if is_left else "|---", end="")
            print(f"{self.data} (b={self.balance})")
            if self.left:
                self.left.print_tree(prefix + ("|   " if is_left else "    "), True)
            if self.right:
                self.right.print_tree(prefix + ("|   " if is_left else "    "))


if __name__ == "__main__":
    # Create a new AVL tree
    avl = AVL_Tree(6)

    # Test multiple insertions
    values = [7, 10, 1, 3, -4, 8]
    for val in values:
        avl = avl.insert(val)  # Important: assign the result back to avl

    print("Initial tree:")
    avl.print_tree()

    # Test search
    print(f"\nIs 10 in the AVL Tree? {avl.search(10)}")
    print(f"Is -1 in the AVL Tree? {avl.search(-1)}")

    # Test height and balance
    print(f"\nTree height: {avl.find_height()}")
    print(f"Root balance: {avl.find_balance()}")

    # Test deletion
    print("\nDeleting 7...")
    avl = avl.delete(7)  # Important: assign the result back to avl
    avl.print_tree()

    print(f"\nNew root balance: {avl.find_balance()}")
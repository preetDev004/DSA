class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.left is None:
            self.left = Node(data)
        elif self.right is None:
            self.right = Node(data)
        else:
            if data < self.data:
                self.left.add_child(data)
            elif data > self.data:
                self.right.add_child(data)

    def pre_order(self, result=[]):
        if self.data:
            result.append(self.data)
            if self.left:
                self.left.pre_order(result)
            if self.right:
                self.right.pre_order(result)
        return result

    def in_order(self, result=[]):
        if self.data:
            if self.left:
                self.left.in_order(result)
            result.append(self.data)
            if self.right:
                self.right.in_order(result)
        return result

    def post_order(self, result=[]):
        if self.data:
            if self.left:
                self.left.post_order(result)
            if self.right:
                self.right.post_order(result)
            result.append(self.data)
        return result

    def display(self, prefix="", is_left=True):
        # Display current node data with prefix indicating left/right
        if prefix:
            connector = "├── " if is_left else "└── "
            print(prefix + connector + str(self.data))
        else:
            print(str(self.data))  # Root node, no prefix

        # Prepare new prefixes for left and right children
        if self.left or self.right:
            if is_left:
                new_prefix = prefix + "│   "
            else:
                new_prefix = prefix + "    "

            # Display left child
            if self.left:
                self.left.display(new_prefix, is_left=True)
            else:
                print(new_prefix + "├── None")

            # Display right child
            if self.right:
                self.right.display(new_prefix, is_left=False)
            else:
                print(new_prefix + "└── None")


class Tree:
    def __init__(self, data):
        self.root = Node(data)
    
    def add_node(self, data):
        self.root.add_child(data)

    def pre_order_traversal(self):
        return self.root.pre_order([])

    def in_order_traversal(self):
        return self.root.in_order([])

    def post_order_traversal(self):
        return self.root.post_order([])

    def display(self):
        self.root.display()


if __name__ == "__main__":
    tree = Tree(10)
    tree.root.add_child(13)
    tree.root.add_child(7)
    tree.root.add_child(9)
    tree.display()

    for i in range(5, 12):
        tree.root.add_child(i)

    tree.root.add_child(4)
    tree.root.add_child(3)

    tree.display()
    print("\nPre-order Traversal:", tree.pre_order_traversal())
    print("In-order Traversal:", tree.in_order_traversal())
    print("Post-order Traversal:", tree.post_order_traversal())

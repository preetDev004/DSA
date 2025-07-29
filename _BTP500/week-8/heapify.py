from Binary_Tree import Tree, Node

def heapify(node):
        if node is None:
            return None

        # Recursively heapify left and right subtrees
        node.left = heapify(node.left)
        node.right = heapify(node.right)

        # Ensure max-heap property
        largest = node
        if node.left and node.left.data > largest.data:
            largest = node.left
        if node.right and node.right.data > largest.data:
            largest = node.right

        # If largest is not the current node, swap and recursively heapify
        if largest != node:
            node.data, largest.data = largest.data, node.data
            if largest == node.left:
                node.left = heapify(node.left)
            else:
                node.right = heapify(node.right)

        return node

if __name__ == "__main__":
    tree = Tree(5)
    tree.add_node(8)
    tree.add_node(7)
    tree.add_node(9)
    tree.add_node(4)
    tree.add_node(-1)
    tree.add_node(10)
    tree.add_node(11)
    tree.display()
    print("---------------------------------------")

    heapify(tree.root)
    tree.display()
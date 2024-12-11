class BST:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if not self.data:
            self.data = data
        elif data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        elif data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
    
    def search(self, data):
        isThere = False
        if self.data:
            if data == self.data:
                isThere = True
            elif self.left and data < self.data:
                isThere = self.left.search(data)
            elif self.right and  data > self.data:
                isThere = self.right.search(data)
        return isThere
        
    def pre_order_print(self, result=[]):
        if self.data:
            result.append(self.data)
            if self.left:
                self.left.pre_order_print()
            if self.right:
                self.right.pre_order_print()
        return result

    def inorder_print(self, result=[]):
        if self.data:
            if self.left:
                self.left.inorder_print()
            result.append(self.data)    
            if self.right:
                self.right.inorder_print()
        return result

    def post_order_print(self, result=[]):
        if self.data:
            if self.left:
                self.left.post_order_print()
            if self.right:
                self.right.post_order_print()
            result.append(self.data)
        return result
    
    def find_height(self):
        height = 0
        if self.data:
            left, right = 0,0 
            if self.left:
                left = self.left.find_height()
            if self.right:
                right = self.right.find_height()
            height = (right if right > left else left) + 1
        return height
    
    def remove(self, data):
        if not self:
            return self
        if data < self.data:
            if self.left:
                self.left = self.left.remove(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.remove(data)
        else:
            if not self.left and not self.right:
                return None
            
            if not self.right:
                return self.left
            elif not self.left:
                return self.right
            
            in_order_successer = self.right.find_min()
            self.data = in_order_successer.data
            self.right = self.right.remove(self.data)
        
        return self
        

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current


if __name__ == "__main__":
    bst = BST(6)
    bst.insert(7)
    bst.insert(10)
    bst.insert(1)
    bst.insert(3)
    bst.insert(-4)
    bst.insert(19)

    # bst.print_tree("")

    print(f"Is 10 in the our BST? {bst.search(10)}")
    print(f"Is -1 in the our BST? {bst.search(-1)}")

    bst.remove(3)
    # bst.print_tree("")

    # print("Printing the BST with breadth first...")
    # bst.breadth_first_print()
    # print()

    print("Printing the BST in order...")
    result = bst.inorder_print()
    print(result)

    print("Printing the BST pre-ordered...")
    result = bst.pre_order_print()
    print(result)

    print("Printing the BST post-ordered...")
    result = bst.post_order_print()
    print(result)

    print(f"The height (max depth) of this tree is: {bst.find_height()}")
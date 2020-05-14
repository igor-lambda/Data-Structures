"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.size = self.size + 1
        self.storage.append(value)

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size = self.size - 1
            return self.storage.pop()


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.size = self.size + 1
        self.storage.insert(0, value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size = self.size - 1
            return self.storage.pop()

    def state_props(self):
        print(self.size, self.storage)


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # This is a recursive
    def insert(self, value):
        if value < self.value:  # we insert lesser values on left
            if not self.left:
                # if there is no left child, make it left child
                self.left = BSTNode(value)
            else:
                self.left.insert(value)  # else keep looking down left branch
        else:
            if not self.right:
                # if no right child, attach as right child, give that value is  eql or greater
                self.right = BSTNode(value)
            else:
                self.right.insert(value)  # else keep looking down right branch

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if not self.right:
            return self.value  # simply return the right most value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.size > 0:  # This works because we will get to q.size 0 when we run out of children
            node = q.dequeue()
            print(node.value)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # The reason a stack switches this from breadth to depth, is that we are processing the
        # left child of the very node we just processed before we look at the right child
        s = Stack()
        s.push(node)
        while s.size > 0: 
            node = s.pop()
            print(node.value)
            if node.left:
                s.push(node.left)
            if node.right:
                s.push(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        # The reason this works is that it's recursive and we ask if node is not None.
        # That way, if a node's left or right is None, we simply return and go down the 
        # call stack
        if node is not None: 
            print(node.value)
            self.pre_order_dft(node.left) 
            self.pre_order_dft(node.right) 

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # The reason switching up the order makes a difference, is because we have to be done
        # traversing both left and right subtrees before we print. This forces us to visit the root
        # last, and to print the right child of a subtree first
        if node is not None: 
            self.post_order_dft(node.left) 
            self.post_order_dft(node.right) 
            print(node.value)


# bst = BSTNode(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# # bst.in_order_print(bst)
# bst.dft_print(bst)

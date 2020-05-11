class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None
        

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next
    
    def set_data(self, new_data):
        self.data = new_data

    def state_props(self):
        print("self.data", self.get_data(), "\nself.next", self.get_next())


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def state_props(self):
        print("size", self.size, "\nhead", self.head.get_data(), "\ntail", self.tail.get_data())

    def increment_size(self):
        self.size = self.size + 1

    def decrement_size(self):
        self.size = self.size - 1

    def is_empty(self):
        return self.head == None
    
    def add_to_end(self, data):
        # this method needs to worry about whether the list is empty or not,
        # because this dictates whether the new node will be placed at the head.
        # or at the next_node of the last node
        node = Node(data)
        self.increment_size()
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
    
    def remove_from_head(self):
        # if list is empty, we can't remove anything, otherwise we need to 
        # turn head to the next node. In the end, we have to return data
        # to the user
        if self.is_empty():
            print('isEmpty')
            return None
        elif self.size == 1:
            print('size=1')
            data = self.head.get_data()
            self.tail = None
            self.head = None
            self.decrement_size()
            return data
        else:
            print('size>1')
            data = self.head.get_data()
            self.head = self.head.get_next()
            self.decrement_size()
            return data

    def add_to_tail(self, data):
        # If list is empty, attach to head, otherwise look for last node, attach as next
        node = Node(data)
        if self.is_empty():
            print('isEmptyAdd')
            self.head = node
            self.tail = node   
        else:
            print('isNotEmptyAdd')
            self.tail.set_next(node)
            self.tail = node
        self.increment_size()




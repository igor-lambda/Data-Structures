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

    def contains(self, data):
        # iterate through list and check for data in each node
        exists = False
        current = self.head
        while current is not None:
            if current.get_data() == data:
                exists = True
            current = current.get_next()
        return exists
    
    def get_max(self):
        # Iterate through list, ask if next data is greater than head data
        # return biggest data
        if self.is_empty():
            return None
        
        max = self.head.get_data()
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
            if current.get_data() > max:
                max = current.get_data()
        return max

    



linked = LinkedList()
print("size", linked.size)
linked.add_to_tail("tail")
linked.state_props()
linked.add_to_tail("tail2")
linked.state_props()
linked.remove_from_head()
linked.state_props()
linked.remove_from_head()
print("size", linked.size)


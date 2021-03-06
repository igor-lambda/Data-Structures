from singly_linked_list import LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.size = self.size + 1
#         self.storage.insert(0, value)

#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else :
#             self.size = self.size - 1
#             return self.storage.pop()

#     def state_props(self):
#         print(self.size, self.storage)
linked = LinkedList()
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = linked
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size = self.size + 1
        # self.storage.insert(0, value)
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else :
            self.size = self.size - 1
            # return self.storage.pop()
            return self.storage.remove_from_head()

    def state_props(self):
        print(self.size, self.storage)


q = Queue()

q.state_props()
q.enqueue("first")
q.state_props()
q.dequeue()
q.state_props()

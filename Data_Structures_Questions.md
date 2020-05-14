Answer the following questions for each of the data structures you implemented as part of this project.

## Stack

1. What is the runtime complexity of `push`?
  
  Constant 

2. What is the runtime complexity of `pop`?

  Constant

3. What is the runtime complexity of `len`?

  Constant

## Queue

1. What is the runtime complexity of `enqueue`?

  Constant  

2. What is the runtime complexity of `dequeue`?

  Constant

3. What is the runtime complexity of `len`?

  Constant

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
  n(logn)

2. What is the runtime complexity of `contains`?
  constant

3. What is the runtime complexity of `get_max`? 
  constant

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
  1

2. What is the runtime complexity of `ListNode.insert_before`?
1

3. What is the runtime complexity of `ListNode.delete`?
1

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
1

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
1

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
1

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
1

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
1

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
1

10. What is the runtime complexity of `DoublyLinkedList.delete`?
1

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    delete only ever does two operations, while splice must copy, and so has both a space and time
    complexity that is linear
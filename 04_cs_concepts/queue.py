class ArrayQueue:
    # front: index == 0
    # back:  index == -1
    def __init__(self):
        self._items = []
    
    # O(1) (avg)
    def enqueue(self, value):
        self._items.append(value)

    # O(1) (avg)
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Cannot dequeue from an empty queue')

        # return_val = self._items[0]
        # self._items = self._items[1:]
        # return return_val
        return self._items.pop(0) # return and remove the first element

    # O(1)
    def front(self):
        if self.is_empty():
            raise IndexError('Cannot look at front element of an empty queue')

        return self._items[0]        

    def is_empty(self):
        return len(self._items) == 0 

class LinkedQueue:
    class _Node:
        def __init__(self, value):
            self.value = value 
            self.next = None

    def __init__(self):
        self._front = None 
        self._back = None 
    
    # O(1)
    def enqueue(self, value):
        node = LinkedQueue._Node(value)

        if self._back is None:
            # special case: queue is empty
            # self._front = self._back = node 
            self._front = node
            self._back = node
        else:
            # the queue is not empty
            self._back.next = node 
            self._back = node
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Cannot dequeue from an empty queue')

        node = self._front 
        self._front = node.next 

        if self._front is None:
            # special case: we just dequeued the last element from the queue
            self._back = None 
        
        return node.value 

    def front(self):
        if self.is_empty():
            raise IndexError('Cannot look at the front element of an empty queue')

        return self._front.value
    
    def is_empty(self):
        return self._front is None 

queue1 = ArrayQueue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
while not queue1.is_empty():
    print(f'{queue1.dequeue() = }')

queue1 = ArrayQueue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
while not queue1.is_empty():
    print(f'{queue1.dequeue() = }')

queue2 = ArrayQueue()
queue2.enqueue(1)
queue2.enqueue(2)
queue2.enqueue(3)
while not queue2.is_empty():
    print(f'{queue2.dequeue() = }')

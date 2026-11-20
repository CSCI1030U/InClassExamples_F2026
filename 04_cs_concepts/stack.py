class ArrayStack:
    def __init__(self):
        self._items = []
    
    def push(self, value):
        self._items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError('cannot pop top element of an empty stack')

        return self._items.pop() # removes and returns the last element
        # return_val = self._items[-1]
        # self._items = self._items[:len(self._items) - 1]
        # return return_val

    def peek(self):
        if self.is_empty():
            raise IndexError('cannot view top element of an empty stack')

        return self._items[-1]

    def is_empty(self):
        # return len(self._items) == 0
        return not self._items

class LinkedStack:
    class _Node:
        def __init__(self, value, next_node):
            self.value = value 
            self.next = next_node

    def __init__(self):
        self._top = None 
    
    def push(self, value):
        self._top = LinkedStack._Node(value, self._top)

    def pop(self):
        if self.is_empty():
            raise IndexError('cannot pop top element of an empty stack')
        
        # 0 -> 1 -> 2 -> 3
        return_val = self._top.value 
        self._top = self._top.next # skip over the first node
        return return_val

    def peek(self):
        if self.is_empty():
            raise IndexError('cannot view top element of an empty stack')

        return self._top.value

    def is_empty(self):
        return self._top is None

stack1 = ArrayStack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
while not stack1.is_empty():
    print(f'{stack1.pop() = }')

stack2 = LinkedStack()
# print(f'{stack2.pop() = }') # error
stack2.push(1)
stack2.push(2)
stack2.push(3)
while not stack2.is_empty():
    print(f'{stack2.pop() = }')

# bracket balancing
def balanced(string):
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'        
    }
    stack = LinkedStack()
    for char in string:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False # unmatched bracket, or wrong closing bracket
    return stack.is_empty()

print(f'{balanced("((1 + 3) * 4) + 1") = }') # True
print(f'{balanced("[(1 + 3) * 4] + 1") = }') # True
print(f'{balanced("([1 + 3) * 4] + 1") = }') # False
print(f'{balanced("[(1 + 3) * 4") = }')
print(f'{balanced("[1 + 3) * 4]") = }')

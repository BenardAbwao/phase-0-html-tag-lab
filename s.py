class Stack:
    """ creates a simple stack class"""
    def __init__(self):
        """ stack container """
        self.stack = []

    def is_empty(self):
        """ checks if the stack is empty"""
        return len(self.stack) < 0
    
    def peak(self):
        """ returns the item on the top of the stack """
        return self.stack[-1]

    def push(self, item):
        """ pushes item to the top of the stack """
        self.stack.append(item)

    def pop(self):
        """ removes the item from the top of the stack """
        return self.stack.pop()

    def print_stack(self):
        """ prints the elements in the stack """
        for item in self.stack:
            print(item, end = ",")






st = Stack()
st.push(34)
st.push(22)
st.push(12)
st.push(23)
st.push(40)

st.print_stack()
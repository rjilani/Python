__author__ = 'rjilani'

class Stack(object):
    def __init__(self): # Initialize the stack
        self.stack = [ ]
    def push(self,object):
        self.stack.append(object)
    def pop(self):
        return self.stack.pop()

    def length(self):
        return len(self.stack)


s = Stack() # Create a stack
s.push("Dave") # Push some things onto it
s.push(42)
s.push([3,4,5])
x = s.pop() # x gets [3,4,5]
print x
y = s.pop()

print y

del s
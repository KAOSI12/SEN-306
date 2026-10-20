
class Stack:
    """
    A Stack data structure that follows
    the Last In, First Out (LIFO) principle.
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """Check whether the stack is empty."""
        return len(self.items) == 0

    def display(self):
        """Display all items in the stack."""
        return self.items

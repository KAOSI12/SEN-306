
class Queue:
    """
    A Queue data structure that follows
    the First In, First Out (FIFO) principle.
    """

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add a customer request to the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the first customer request."""
        if self.is_empty():
            return None
        return self.items.pop(0)

    def front(self):
        """View the first customer request."""
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        """Check whether the queue is empty."""
        return len(self.items) == 0

    def display(self):
        """Display all customer requests."""
        return self.items

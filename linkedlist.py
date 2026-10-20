
class Node:
    """Represents one node in the linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Manages completed customer requests."""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a new record to the end of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def delete(self, data):
        """Delete a record from the linked list."""
        current = self.head
        previous = None

        while current is not None:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True

            previous = current
            current = current.next

        return False

    def search(self, data):
        """Search for a record in the linked list."""
        current = self.head

        while current is not None:
            if current.data == data:
                return True
            current = current.next

        return False

    def display(self):
        """Display all records in the linked list."""
        records = []
        current = self.head

        while current is not None:
            records.append(current.data)
            current = current.next

        return records

    def is_empty(self):
        """Check whether the linked list is empty."""
        return self.head is None

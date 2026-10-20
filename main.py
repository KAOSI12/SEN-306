
from stack import Stack
from queue import Queue
from linkedlist import LinkedList


class CustomerServiceSystem:
    """Main system for managing customer service requests."""

    def __init__(self):
        self.action_stack = Stack()
        self.request_queue = Queue()
        self.completed_requests = LinkedList()

    def add_request(self):
        """Add a customer complaint to the queue."""
        customer = input("Enter customer name: ").strip()
        complaint = input("Enter complaint: ").strip()

        if not customer or not complaint:
            print("Customer name and complaint cannot be empty.")
            return

        request = {
            "customer": customer,
            "complaint": complaint
        }

        self.request_queue.enqueue(request)
        self.action_stack.push(("add", request))

        print("Customer request added successfully.")

    def process_request(self):
        """Process the first customer request."""
        if self.request_queue.is_empty():
            print("No pending customer requests.")
            return

        request = self.request_queue.dequeue()
        self.completed_requests.append(request)
        self.action_stack.push(("process", request))

        print("Request processed successfully.")
        print("Customer:", request["customer"])
        print("Complaint:", request["complaint"])

    def view_pending(self):
        """Display all pending customer requests."""
        print("\n--- Pending Customer Requests ---")

        requests = self.request_queue.display()

        if not requests:
            print("No pending requests.")
            return

        for request in requests:
            print(request)

    def view_completed(self):
        """Display all completed customer requests."""
        print("\n--- Completed Customer Requests ---")

        requests = self.completed_requests.display()

        if not requests:
            print("No completed requests.")
            return

        for request in requests:
            print(request)

    def undo_action(self):
        """Undo the most recent recorded action."""
        if self.action_stack.is_empty():
            print("No action available to undo.")
            return

        action, request = self.action_stack.pop()

        if action == "add":
            self.request_queue.items.remove(request)
            print("Last added request has been undone.")

        elif action == "process":
            self.completed_requests.delete(request)
            self.request_queue.items.insert(0, request)
            print("Last processed request has been restored.")

    def run(self):
        """Display the main menu and run the application."""
        while True:
            print("\n===== CUSTOMER SERVICE MANAGEMENT SYSTEM =====")
            print("1. Add Customer Request")
            print("2. Process Customer Request")
            print("3. View Pending Requests")
            print("4. View Completed Requests")
            print("5. Undo Last Action")
            print("6. Exit")

            choice = input("Select an option (1-6): ")

            if choice == "1":
                self.add_request()

            elif choice == "2":
                self.process_request()

            elif choice == "3":
                self.view_pending()

            elif choice == "4":
                self.view_completed()

            elif choice == "5":
                self.undo_action()

            elif choice == "6":
                print("Thank you for using the system.")
                break

            else:
                print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    system = CustomerServiceSystem()
    system.run()

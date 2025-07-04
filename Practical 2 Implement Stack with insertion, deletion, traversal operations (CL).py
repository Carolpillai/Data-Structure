class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def display_menu():
    print("\n====== STACK OPERATIONS MENU ======")
    print("1. Insert (Push)")
    print("2. Delete (Pop)")
    print("3. Peek")
    print("4. Is Empty?")
    print("5. Get Size")
    print("6. Traverse (Display Stack)")
    print("7. Exit")
    print("====================================")

def main():
    stack = Stack()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            element = input("Enter the element to push: ").strip()
            if element:
                stack.push(element)
                print(f"'{element}' pushed onto the stack.")
            else:
                print("Please enter a valid element.")
        
        elif choice == '2':
            try:
                popped = stack.pop()
                print(f"Popped item: {popped}")
            except IndexError as e:
                print(f"Error: {e}")

        elif choice == '3':
            try:
                top = stack.peek()
                print(f"Top item: {top}")
            except IndexError as e:
                print(f"Error: {e}")

        elif choice == '4':
            if stack.is_empty():
                print("The stack is empty.")
            else:
                print("The stack is not empty.")

        elif choice == '5':
            print(f"Size of the stack: {stack.size()}")

        elif choice == '6':
            print(f"Stack content: {stack}")

        elif choice == '7':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()

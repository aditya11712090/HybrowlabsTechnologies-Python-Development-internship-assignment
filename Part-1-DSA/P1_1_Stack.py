class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def push(self, item):
        if self.top == self.size - 1:
            print("Stack Overflow!")
        else:
            self.top += 1
            self.stack[self.top] = item

    def pop(self):
        if self.top == -1:
            print("Stack Underflow!")
        else:
            item = self.stack[self.top]
            self.top -= 1
            return item

    def peek(self):
        if self.top == -1:
            print("Stack is empty!")
        else:
            item = self.stack[self.top]
            return item

    def is_empty(self):
        if self.top == -1:
            print("Stack is empty!")
            return True
        else:
            print("Stack is not empty!")
            return False

    def display(self):
        if self.top == -1:
            print("Stack is empty!")
        else:
            print("Elements in the stack:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

stack_size = int(input("Enter the size of the stack: "))
stack = Stack(stack_size)

while True:
    print("\nChoose an option:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Is Empty?")
    print("5. Display")
    print("6. Quit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        items = input("Enter the items to push, separated by spaces: ").split()
        for item in items:
            stack.push(item)
        print("Pushed items to the stack")
    elif choice == 2:
        item = stack.pop()
        if item:
            print(f"Popped {item} from the stack")
    elif choice == 3:
        item = stack.peek()
        if item:
            print(f"The top item is {item}")
    elif choice == 4:
        stack.is_empty()
    elif choice == 5:
        stack.display()
    elif choice == 6:
        break
    else:
        print("Invalid choice!")

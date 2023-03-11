class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self, size):
        self.front = None
        self.rear = None
        self.size = size
        self.count = 0
        
    def enqueue(self, item):
        if self.count == self.size:
            print("Queue is full.")
            return
        new_node = Node(item)
        if self.rear is None:
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.count += 1
        print(f"{item} added to queue.")
        
    def dequeue(self):
        if self.count == 0:
            print("Queue is empty.")
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.count -= 1
        return item
    
    def peek(self):
        if self.count == 0:
            print("Queue is empty.")
            return None
        return self.front.data
    
    def is_empty(self):
        return self.count == 0
    
    def display(self):
        if self.count == 0:
            print("Queue is empty.")
            return
        current = self.front
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()
        

size = int(input("Enter size of queue: "))
queue = Queue(size)

while True:
    print("\nChoose operation:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Is empty?")
    print("5. Display")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        for i in range(queue.size - queue.count):
            item = input(f"Enter item {i+1}: ")
            queue.enqueue(item)
    elif choice == 2:
        item = queue.dequeue()
        if item is not None:
            print(f"{item} dequeued from queue.")
    elif choice == 3:
        item = queue.peek()
        if item is not None:
            print(f"Front item: {item}")
    elif choice == 4:
        if queue.is_empty():
            print("Queue is empty.")
        else:
            print("Queue is not empty.")
    elif choice == 5:
        queue.display()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Try again.")

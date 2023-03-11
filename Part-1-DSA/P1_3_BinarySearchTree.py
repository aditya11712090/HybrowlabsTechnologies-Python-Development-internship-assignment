class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.count = 0
    
    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)
        self.count += 1
        
    def _insert(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(val, node.left)
        elif val > node.val:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(val, node.right)
    
    def search(self, val):
        return self._search(val, self.root)
        
    def _search(self, val, node):
        if node is None:
            return False
        elif val == node.val:
            return True
        elif val < node.val:
            return self._search(val, node.left)
        else:
            return self._search(val, node.right)
        
    def size(self):
        return self.count
    
    def delete(self, val):
        if self.root is None:
            return False
        else:
            self.root, deleted = self._delete(val, self.root)
            if deleted:
                self.count -= 1
            return deleted
    
    def _delete(self, val, node):
        if node is None:
            return node, False
        elif val == node.val:
            if node.left is None and node.right is None:
                return None, True
            elif node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            else:
                successor = self._find_min(node.right)
                node.val = successor.val
                node.right, _ = self._delete(successor.val, node.right)
                return node, True
        elif val < node.val:
            node.left, deleted = self._delete(val, node.left)
        else:
            node.right, deleted = self._delete(val, node.right)
        return node, deleted
    
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def display(self):
        self._display(self.root)
    
    def _display(self, node):
        if node is not None:
            self._display(node.left)
            print(node.val, end=' ')
            self._display(node.right)
    
# menu interface
bst = BinarySearchTree()
while True:
    print("\nBinary Search Tree Operations:")
    print("1. Insert element(s)")
    print("2. Delete element")
    print("3. Search element")
    print("4. Size of tree")
    print("5. Display tree")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        n = int(input("Enter the number of elements to be inserted: "))
        for i in range(n):
            val = int(input("Enter element: "))
            bst.insert(val)
    elif choice == 2:
        val = int(input("Enter the element to be deleted: "))
        if bst.delete(val):
            print(val, "deleted from tree.")
        else:
            print(val, "not found")
    elif choice == 3:
        val = int(input("Enter the element to be searched: "))
        if bst.search(val):
            print(val, "found in tree.")
        else:
            print(val, "not found in tree.")
        
    elif choice == 4:
        print("Size of tree:", bst.size())
        
    elif choice == 5:
        print("Binary Search Tree (in-order):")
        bst.display()
        
    elif choice == 6:
        break
        
    else:
        print("Invalid choice. Please try again.")
    

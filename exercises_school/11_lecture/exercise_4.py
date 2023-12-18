class Node:
    """
    A simple class representing a node in a linked list.

    Attributes:
        value: The value stored in the node.
        next: A reference to the next node in the linked list (default is None).
    """
    def __init__(self, value, next=None):
        """
        Initialize a new Node.

        Args:
            value: The value to be stored in the node.
            next: Reference to the next node (default is None).
        """
        self.value = value
        self.next = next

    def has_next_node(self):
        """
        Check if the node has a next node.

        Returns:
            True if there is a next node, False otherwise.
        """
        return self.next is not None


class Stack:
    """
    A class representing a stack data structure using linked nodes.

    Attributes:
        size: The current size of the stack.
        head: The top element of the stack.
    """
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.size = 0
        self.head = None

    def add(self, value):
        """
        Add a new element to the top of the stack.

        Args:
            value: The value to be added to the stack.
        """
        current_head = self.head
        self.head = Node(value)
        self.head.next = current_head
        self.size += 1

    def pop(self):
        """
        Remove and return the top element from the stack.

        Returns:
            The value of the removed element.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        current_head = self.head
        self.head = current_head.next
        self.size -= 1
        return current_head.value

    def pop_all(self):
        """
        Remove and return all elements from the stack.

        Returns:
            A list of all the elements in the stack, in the order they were removed.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        list_of_values = []
        node = self.head
        while node is not None:
            list_of_values.append(node.value)
            node = node.next
        self.clear()
        return list_of_values

    def clear(self):
        """
        Clear the stack, removing all elements.
        """
        self.head = None
        self.size = 0

    def count(self):
        """
        Get the current size of the stack.

        Returns:
            The number of elements in the stack.
        """
        return self.size

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.size == 0

    def __len__(self):
        """
        Get the current size of the stack.

        Returns:
            The number of elements in the stack.
        """
        return self.size

    def __getitem__(self, key):
        """
        Get the value of the element at the specified index.

        Args:
            key: The index of the element to get.

        Returns:
            The value of the element at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if key < 0 or key >= self.size:
            raise IndexError("Index out of range")
        node = self.head
        for _ in range(key):
            node = node.next
        return node.value

    def __setitem__(self, key, value):
        """
        Set the value of the element at the specified index.

        Args:
            key: The index of the element to set.
            value: The value to set.

        Raises:
            IndexError: If the index is out of range.
        """
        if key < 0 or key >= self.size:
            raise IndexError("Index out of range")
        node = self.head
        for _ in range(key):
            node = node.next
        node.value = value
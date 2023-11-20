class Node:
    """
    Node class represents an element in a linked list.

    Attributes:
    - value: The value stored in the node.
    - next: Reference to the next node in the linked list.
    """

    def __init__(self, value, next=None):
        """
        Initialize a new Node with the given value and optional next node reference.

        Args:
        - value: The value to be stored in the node.
        - next: (Optional) Reference to the next node in the linked list.
        """
        self.value = value
        self.next = next

    def get_next(self):
        """
        Get the next node in the linked list.
        """
        return self.next

    def get_value(self):
        """
        Get the value stored in the node.
        """
        return self.value


class LinkedList:
    """
    LinkedList class represents a singly-linked list data structure.

    Attributes:
    - head: Reference to the first node in the linked list.
    """

    def __init__(self):
        """
        Initialize an empty linked list with no nodes.

        The head is initially set to None.
        """
        self.head = None

    def add_value(self, value):
        """
        Add a new node with the given value to the beginning of the linked list.

        Args:
        - value: The value to be added to the linked list.
        """
        if self.head is None:
            # If the linked list is empty, set the head to a new node with the given value.
            self.head = Node(value)
        else:
            # If the linked list is not empty, create a new node and make it the new head,
            # with the current head as its next node.
            current = self.head
            self.head = Node(value, current)


    def get_all(self):
        """
        Generator function to iterate and yield values of all nodes in the linked list.

        Yields:
        - The value of each node in the linked list.
        """
        current = self.head
        while current is not None:
            yield current.value
            current = current.next



# test it
l = LinkedList()
l.add_value(1)
l.add_value(2)
l.add_value(3)
l.add_value(4)

for i in l.get_all():
    print(i)

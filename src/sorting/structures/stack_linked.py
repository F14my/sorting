class Node:
    """The Node class for linked list"""
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None

class Stack:
    """The Stack class for linked list"""
    def __init__(self) -> None:
        """Initialize the Stack class"""
        self.head = None

    def push(self, x: int) -> None:
        """Push the value x to the top of the stack"""
        node = Node(x)
        node.next = self.head
        self.head = node

    def pop(self) -> int:
        """Pop the top of the stack and return its value"""
        if self.head is None:
            raise ValueError("Stack is empty")
        node = self.head
        self.head = self.head.next
        return node.value

    def peek(self) -> int:
        """Get the top of the stack and return its value"""
        if self.head is None:
            raise ValueError("Stack is empty")
        node = self.head
        return node.value

    def is_empty(self) -> bool:
        """Check if the stack is empty"""
        return self.head is None

    def __len__(self) -> int:
        """Get the length of the stack"""
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def min(self) -> int:
        """Get the minimum value in the stack"""
        if self.head is None:
            raise ValueError("Stack is empty")
        node = self.head
        min_value = node.value
        while node.next:
            node = node.next
            if node.value < min_value:
                min_value = node.value
        return min_value

    def __str__(self) -> str:
        """Get the string representation of the stack"""
        result = []
        node = self.head
        while node:
            result.append(str(node.value))
            node = node.next
        return " -> ".join(result)



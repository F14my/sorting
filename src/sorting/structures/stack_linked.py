class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, x: int) -> None:
        node = Node(x)
        node.next = self.head
        self.head = node

    def pop(self) -> int:
        if self.head is None:
            raise ValueError("Stack is empty")
        node = self.head
        self.head = self.head.next
        return node.value

    def peek(self) -> int:
        if self.head is None:
            raise ValueError("Stack is empty")
        node = self.head
        return node.value

    def is_empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def min(self) -> int:
        if self.head is None:
            raise ValueError("Stack is empty")
        node = self.head
        min_value = node.value
        while node.next:
            node = node.next
            min_value = node.value
        return min_value

    def __str__(self) -> str:
        result = []
        node = self.head
        while node:
            result.append(str(node.value))
            node = node.next
        return " -> ".join(result)



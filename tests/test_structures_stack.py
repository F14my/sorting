from src.sorting.structures.stack_linked import Stack

stack = Stack()
def test_stack_push():
    stack.push(5)
    stack.push(6)
    stack.push(7)
    assert str(stack) == "7 -> 6 -> 5"

def test_stack_pop():
    stack.pop()
    assert str(stack) == "6 -> 5"

def test_stack_peek():
    assert stack.peek() == 6
    assert str(stack) == "6 -> 5"

def test_stack_is_empty():
    assert stack.is_empty() == False

def test_stack_length():
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    assert len(stack) == 6

def test_stack_min():
    stack.push(-2)
    stack.push(-3)
    stack.push(8)
    assert stack.min() == -3

def test_stack_str():
    stack.push(5)
    stack.push(6)
    assert str(stack) == "6 -> 5 -> 8 -> -3 -> -2 -> 8 -> 7 -> 6 -> 5 -> 6 -> 5"
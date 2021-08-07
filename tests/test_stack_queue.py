
import pytest

from data_structures_algorth.challenge_stack_and_queue.stack_queue import Stack, Queue, StackIsEmptyException, QueueIsEmptyException

##Can successfully instantiate an empty stack:

def test_stack_instantiated():
    assert Stack()

#Can successfully push onto a stack:

def test_push_value_stack():
    stack = Stack()
    stack.push(2)
    actual= stack.top.value
    expected = 2
    assert actual == expected

#Can successfully push multiple values onto a stack
def test_push_multiple_values_stack():
    stack = Stack()
    stack.push(2)
    stack.push(3)
    actual= stack.top.value
    expected = 3
    assert actual == expected

#Can successfully pop off the stack
def test_pop_value_stack():
    stack = Stack()
    stack.push(2)
    
    actual= stack.pop()
    expected = 2
    assert actual == expected

#Calling pop on empty stack raises exception
def test_pop_empty_stack():
    stack = Stack()
    with pytest.raises(StackIsEmptyException) as excinfo:
        stack.pop()
    assert "Hey I cannot do the pop, stack is empty !" == str(excinfo.value)

#Can successfully empty a stack after multiple pops
def test_multiple_pops_stack():
    stack = Stack()
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
   
    assert stack.top == None

#can check if the stack is empty
def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty()

#can check if the stack is not empty
def test_stack_is_not_empty():
    stack = Stack()
    stack.push(5)
    assert not stack.is_empty()

#Can successfully peek the next item on the stack
def test_peek_stack():
    stack = Stack()
    stack.push(7)
    actual= stack.peek()
    expected = 7
    assert actual == expected

#Calling peek on empty stack raises exception
def test_peek_empty_stack():
    stack = Stack()
    with pytest.raises(StackIsEmptyException ) as excinfo:
        stack.peek()
    assert 'Hey I cannot peek, stack is empty !' == str(excinfo.value)

#Can successfully instantiate an empty queue
def test_queue_instantiation():
    assert Queue()

#Can successfully enqueue into a queue
def test_enqueue_value():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    actual = queue.front.value
    expected = 1
    assert actual == expected

#Can successfully dequeue out of a queue the expected value
def test_dequeue_value():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    actual = queue.dequeue()
    expected = 1
    assert actual == expected

#Calling dequeue on empty queue raises exception
def test_dequeue_empty_stack():
    queue = Queue()
    with pytest.raises(QueueIsEmptyException) as excinfo:
        queue.dequeue()
    assert "Hey I cannot dequeue, queue is empty !" == str(excinfo.value)

#can check if the queue is empty
def test_queue_is_empty():
    queue = Queue()
    assert queue.is_empty()

#can check if the queue is not empty
def test_queue_is_not_empty():
    queue = Queue()
    queue.enqueue(5)
    assert not queue.is_empty()

#Can successfully peek the next item on the queue
def test_peek_Queue():
    queue = Queue()
    queue.enqueue(7)
    queue.enqueue(6)
    actual= queue.peek()
    expected = 7
    assert actual == expected

#Calling peek on empty stack raises exception
def test_peek_empty_queue():
    queue = Queue()
    with pytest.raises(QueueIsEmptyException ) as excinfo:
        queue.peek()
    assert 'Hey I cannot peek, queue is empty !' == str(excinfo.value)
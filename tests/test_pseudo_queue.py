
import pytest
from data_structures_algorth.challenge_pseudo_queue.pseudo_queue import PseudoQueue
from data_structures_algorth.challenge_stack_and_queue.stack_queue import  QueueIsEmptyException, StackIsEmptyException

#Can successfully enqueue into a pseudoqueue
def test_pseudo_enqueue_value():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    actual = queue.front.top.value
    expected = 2
    assert actual == expected



#Can successfully dequeue out of a queue the expected value
def test_pseudo_dequeue_value():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    actual = queue.dequeue()
    expected = 1
    assert actual == expected

#Calling dequeue on empty queue raises exception
def test_pseudo_dequeue_empty_stack():
    queue = PseudoQueue()
    with pytest.raises(StackIsEmptyException) as excinfo:
        queue.dequeue()
    assert "Hey I cannot do the pop, stack is empty !" == str(excinfo.value)

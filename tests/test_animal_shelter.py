
import pytest
from data_structures_algorth.challenge_stack_queue_animal.animal_shelter import AnimalShelter
from data_structures_algorth.challenge_stack_and_queue.stack_queue import QueueIsEmptyException

#Can successfully enqueue dog into a Animal shelter
def test_shelter_enqueue_dog_value():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('cat')
    actual = shelter.dog.front.value
    expected = 'dog'
    assert actual == expected

#Can successfully enqueue cat into a Animal shelter
def test_shelter_enqueue_cat_value():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('cat')
    actual = shelter.cat.front.value
    expected = 'cat'
    assert actual == expected
    
#Can successfully dequeue dog from a Animal shelter
def test_shelter_dequeue_dog_value():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('cat')
    actual = shelter.dequeue('dog')
    expected = 'dog'
    assert actual == expected

#Can successfully dequeue cat from a Animal shelter
def test_shelter_dequeue_cat_value():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('cat')
    actual = shelter.dequeue('cat')
    expected = 'cat'
    assert actual == expected

#Cannot dequeue cat from a Animal shelter if the cat queue is empty
def test_shelter_dequeue_empty_cat_value():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('cat')
    shelter.dequeue('cat')
    shelter.dequeue('cat')
    with pytest.raises(QueueIsEmptyException) as excinfo:
        shelter.dequeue('cat')
    assert "Sorry there are no cats waiting in our shelter" == str(excinfo.value)

#Cannot dequeue cat from a Animal shelter if the dog queue is empty
def test_shelter_dequeue_empty_dog_value():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.dequeue('dog')
    shelter.dequeue('dog')
    with pytest.raises(QueueIsEmptyException) as excinfo:
        shelter.dequeue('dog')
    assert "Sorry there are no dogs waiting in our shelter" == str(excinfo.value)

#Cannot dequeue animal other than cat or dog from a Animal shelter 
def test_shelter_dequeue_diff_animal_value():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    
    actual = shelter.dequeue('bird')

    assert actual == None

#Cannot enqueue animal other than cat or dog to a Animal shelter 
def test_shelter_enqueue_diff_animal_value():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    
    with pytest.raises(Exception) as excinfo:
        shelter.enqueue('bear')
    assert 'No other animals are allowed!!' == str(excinfo.value)

    
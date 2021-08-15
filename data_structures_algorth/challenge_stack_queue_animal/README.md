
# Challenge Summary

- Creation of a class called AnimalShelter which holds only dogs and cats and The shelter operates using a first-in, first-out approach.
- It has the enqueue method: which take an Argument: animal,animal can be either a dog or a cat object.
- It has the dequeue method which take the Argument: pref,pref can be either "dog" or "cat"
       


## Whiteboard Process
https://miro.com/welcomeonboard/SnlUUmFHUlA3UTFJVkwxWGVuRG1tWExYUEJGbWRrY2xGNkVJbW8zVXdGanN2ZFdCNmJYRmR5eHlBNFh0Z1o5N3wzMDc0NDU3MzYxNzU4NzExMTcx

## Approach & Efficiency:

- Big O(1) in term of time and space complexity.

## Solution

- enqueue:
1- create an instance of the queue class and assign it to the dog object and another instance for the cat object
2- create the method of the enqueue with the argument of the animal passed and inside it check which animal is passed and according to it apply the enqueue method on the dog object or dog object

- dequeue:
- create dequeue method and inside it apply the dequeue method on the cat or dog object according to which passed with the argument check before this if the each of the instances are not empty.

## PR:
-

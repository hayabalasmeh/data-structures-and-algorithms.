# Stacks and Queues

- Stack and Queue are both node based data structures that implement the approach of O(1) in terms of time complexity.
_
## Challenge:

- Creating a Node class that has properties for the value stored in the Node, and a pointer to the next node.

- Buildin Stack and Queue classes and their methods.

## Approach & Efficiency:

- Big O notation of O(1) in term of time and space complexity.

## API

### Stack:

1- Push method:
- create a node with a passed value and push this node to the top of the stack

2- Pop method:
- return the value of the node that the top pointer was pointing to, and remove this node from the stack

3- Peek: will take a look at what the top pointer is pointing and return its value without modifying the stack 

4- Is empty method:
will ckeck if the stack is empty or not by checking if the top pointer is pointing to none or not


### Queue:

1- Enqueue method:
- create a node with a passed value and push this node to the top of the queue

2- Dequeue method:
- return the value of the node that the top pointer was pointing to, and remove this node from the queue

3- Peek: will take a look at what the top pointer is pointing and return its value without modifying the queue

4- Is empty method:
will ckeck if the queue is empty or not by checking if the top pointer is pointing to none or not

## PR link:
https://github.com/hayabalasmeh/data-structures-and-algorithms./pull/7
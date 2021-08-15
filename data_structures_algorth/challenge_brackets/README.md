# Author Haya Balasmeh

## Challenge Summary

## Whiteboard

[whiteboard](https://miro.com/welcomeonboard/TnB6V1Bpa282ZWQyaTJyTGk2cjRYY2w5TmJWbExpWGtCZXphMlpsWjJGa2NyT1J2OGhJYXRYcmJPaHp3YTNrT3wzMDc0NDU3MzYxNzU4NzExMTcx)

## Approach & Efficiency

- Big O(n) in term of time and space complexity.

## Solution

1-create a function called validate brackets that take an input of a string.
2- create an instance of the stack class.
3- check if the character inside the string are opening character then push it inside the stack instance .
4- if the brackets are closing brackets then check the top value of the stack instance with the character and check if they are from the same type then pop the top value .
5- if none of the types matched then return false
6- if the string characters of the same type poped then check if the stack is empty then all of them are matching else return false.

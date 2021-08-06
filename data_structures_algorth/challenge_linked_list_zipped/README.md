# Challenge Summary
-Writing a function that Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.

## Whiteboard Process
- https://miro.com/welcomeonboard/MkV2V2pHd1d5NXY2YVN0ZWdPVU1SZk9maXNuUzhoODYzVkFUZGZtdENtOGRlV1d0bmU3NEdjemlzV0FrOU94NHwzMDc0NDU3MzYxNzU4NzExMTcx

## Approach & Efficiency
- Big O notation : 
- time O(n)
-space = O(1)

## solution:

-if both were not empty then check if the the first list is empty then return the second
- then check if the second list is empty then return the first list
- create a 2 variables that has the value of none in order to store the refrence of the next pointers
- check if the next pointer of the first list head is none then assign it to point to the second list head .

-assign the first list head next pointer to the second list head
-return the first list
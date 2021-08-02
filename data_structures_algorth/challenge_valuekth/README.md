# Challenge Summary
-Writing a method that Return the node’s value that is k places from the tail of the linked list.

## Whiteboard Process
- https://miro.com/welcomeonboard/cEppekMxWUZGdzNQVDVlSEdiSDNpUHdBQ0I3Z3labDk0eVhZT1R5VzZwbWxTM01MTnJLcnZqUjV3THRtTmtGZ3wzMDc0NDU3MzYxNzU4NzExMTcx

## Approach & Efficiency
- Big O notation : 
- O(n)

## Solution
- create the method
- Add variables that has the value of the list length(nodes number) by looping inside the output of traversing through the list.

- Add a condition to check if the value of the k is greater than length-1, also if k is less than 0 and raise an exception telling it's out of range.
- Add a loop while the k is larger than 0 or equal to it .
- check if the counter number equal to the k then return the value of the current node.
if not keep looping and decreasing the value of the counter untill reach the one wanted.


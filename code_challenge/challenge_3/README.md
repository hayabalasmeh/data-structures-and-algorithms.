#  Binary Search of Sorted Array
- a function which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available ,it will return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array..

## Whiteboard Process:

## This the whiteboard link :

https://miro.com/app/board/o9J_l5ffISA=/

## Approach & Efficiency :

- created the function for the binary search purpose.
- declaring three variables one for the start point index and one for the end point index and one for the middle index.
- loop through the values using the while as long as the start index is lower than the end index.
- add a value for the middle index by dividing the summation of the start and end indexes by 2.
- then check if the target value equal the value at the middle index if not,
- check if the target value is bigger than the value at the middle index then ignore the left part meaning make the start index equal to the middle index plus one , else non of the previous conditions then the target will be smaller than the value at the middle index in this case make the end index equal to the middle index -1.
- in case no value found return -1.
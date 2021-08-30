# The merge sort

- MergeSort is a sorting algorithm that split the array into left and right array and sort them then merge them in ascending order.


## Pseudocode

`ALGORITHM Mergesort(arr)`
    `DECLARE n <-- arr.length`

   `if n > 1`
    `DECLARE mid <-- n/2`
    `DECLARE left <-- arr[0...mid]`
    `DECLARE right <-- arr[mid...n]`
    `// sort the left side`
    `Mergesort(left)`
    `// sort the right side`
    `Mergesort(right)`
    `// merge the sorted left and right sides together`
    `Merge(left, right, arr)`

## Trace

- Sample Array: `[8,4,23,42,16,15]`


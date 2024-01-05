## **Space Complexity**

Space complexity refers to the amount of memory or storage space an algorithm requires to solve a problem as a function of the input size. It consists of two main components:

- **Auxiliary Space**: This refers to the extra space used by the algorithm itself, apart from the input. It includes the memory required by the variables, data structures, and other internal components of the algorithm.

- **Space Used for Input Values**: This is the memory required to store the input data that the algorithm operates on.

So, the overall space complexity of is the sum of the auxiliary space and the space used for input values:

`Space Complexity = O(1) (Auxiliary Space) + O(N) (Space Used for Input Values) = O(N)`

Other notes:
- Variables count as space, but if you’re storing scalars in them, then their space usage is constant. So if you’re not allocating any new arrays or objects, then you’ve got O(1) space complexity. For example: a `for` loop uses O(1) space (same amount of space regardless of array size, since you're swapping out for the same space), but O(n) time.
- In Python, slicing lists does not generate copies of the objects in the list; it just copies the references to them. So if you have a function that makes a slice of an input array, that operation alone uses O(1) auxiliary space.

## **Time Complexity**




| Syntax      | Array/List  | String(Immutable)      | 
| ----------- | ----------- | ----------- | 
| Appending to end | O(1)| O(n) | 
| Popping from end | O(1)| O(n) | 
| Insertion (not from end) | O(n) | O(n) |
| Deletion (not from end) | O(n) | O(n) |
| Modifying an element | O(1) | O(n) |
| Random access | O(1) | O(1) |

## **Other Notes**

- **Amortized analysis** is a method for analyzing a given algorithm's complexity, or how much of a resource, especially time or memory, it takes to execute. The motivation for amortized analysis is that looking at the worst-case run time can be too pessimistic. Instead, amortized analysis averages the running times of operations in a sequence over that sequence.
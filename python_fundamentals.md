[Markdown Syntax Guide](https://www.markdownguide.org/basic-syntax/)

## **Errors & Exception Handling**

There are three kinds of errors:

1. **Syntax Errors**: raised by interpreter when it encounters syntax it doesn't understand during parsing
2. **Runtime Errors**: occurs while our program is already running
3. **Logical Errors**

### Handling raised exceptions

Raising an error to check if a value is numeric:

    try:
        x + 1
    except ValueError as customer_error_var:
        print(f"An exception occurred. Here are the error details: {customer_error_var}")

---

## **Lists (Dynamic Arrays)**

You can look at ranges with slice syntax: `li[start:end:step]`
The start index is included, the end index is not (It's a closed/open range for you mathy types) - use any combination of these to make advanced slices.
For example, given `li = [1, 2, 4, 3]`:

```
li[-1]    # Return element at very last index => [3] (Good way to grab the most recent element you appended to a list)
li[1:-1]  # Return list starting from index 1 up until last index => [2, 4]
li[1:3]   # Return list from index 1 to 3 => [2, 4]
li[2:]    # Return list starting from index 2 => [4, 3]
li[:3]    # Return list from beginning until index 3  => [1, 2, 4]
li[::2]   # Return list selecting elements with a step size of 2 => [1, 4]
li[::-1]  # Return list in reverse order => [3, 4, 2, 1]
```


This is example syntax for modifying one element in a nested list:

    my_list[inner_list_index][element_index] = new_value

The `sorted()` function returns a new sorted (ascending order) list from an iterable:

    sorted([5, 2, 3, 1, 4])
    # Output: [1, 2, 3, 4, 5]

The `.sort()` method modifies the list in-place (and returns `None` to avoid confusion). Usually it’s less convenient than sorted() - but if you don’t need the original list, it’s slightly more efficient. Time complexity is O(n log n) for average and worst cases.

    a = [5, 2, 3, 1, 4]
    a.sort()
    # a is now [1, 2, 3, 4, 5]

Both `list.sort()` and `sorted()` accept a reverse parameter with a boolean value.

Both `list.sort()` and `sorted()` also take a key parameter to specify a function (or other callable) to be called on each list element prior to making comparisons. The value of the key parameter should be a function (or other callable) that takes a single argument and returns a key to use for sorting purposes. This technique is fast because the key function is called exactly once for each input record.

    def sort_second(val):
	    return val[1]
    my_list1 = [(1, 2), (3, 3), (1, 1)]
    my_list1.sort(key=sort_second)
    print(my_list1)
    my_list1.sort(key=sort_second, reverse=True)
    print(my_list1)


The `.remove()` method will remove the **first instance** of a value in a list.

    list = [1, 2, 3, 1]
    list.remove(1) # Output: [2, 3, 1]

The `.pop()` method removes an element at a given index, and will also return the removed item.

    numbers = [10, 20, 30, 40]
    ten = numbers.pop(0)
    print(ten) # Output: 10

You can also use the `del` keyword in Python to remove an element or slice from a list.

    numbers = [50, 60, 70, 80]
    del numbers[1:2]
    print(numbers) # [50, 70, 80]

One other method from removing elements from a list is to take a slice of the list, which excludes the index or indexes of the item or items you are trying to remove. For instance, to remove the first two items of a list, you can do

    list = list[2:]

---

## **Tuples**

A **tuple** represents a sequence of any objects separated by commas and enclosed in parentheses. A tuple is an immutable object, which means it cannot be changed, and we use it to represent fixed collections of items.

---

## **Dictionaries (Hash Maps/Tables) & Sets**

A **dictionary (also called hash map or hash table in other languages)** must have a key that is **immutable**, i.e. a string or tuple. Fun trick: in Python, if you want to use an array i.e. list (mutable) as a hash key, you can convert it to a **tuple** with `tuple(arr)` or to a string of comma-separated values, since both tuples and strings are immutable. This can come in handy if you want to create a key from an ordered collection of elements, since arrays/lists can be sorted and maintain their order. 

A **set (also called a hash set in other languages)** uses the same mechanism for hashing keys into integers as a dictionary, except that sets do not map their keys to anything: a set is just a collection of unique keys (basically a dictionary without values). Sets are more convenient to use when you only care about checking if elements exist. You can add, remove, and check if an element exists in a set all in O(1) time. 

Declaration: a hash map is declared like any other variable. The syntax is {}

    hash_map = {}

If you want to initialize it with some key value pairs, use the following syntax:

    hash_map = {1: 2, 5: 3, 7: 2}

Checking if a key exists: simply use the `in` keyword

    1 in hash_map # True
    9 in hash_map # False

Accessing a value given a key: use square brackets, similar to an array.

    hash_map[5] # 3

Adding or updating a key: use square brackets, similar to an array.
If the key already exists, the value will be updated

    hash_map[5] = 6

If the key doesn't exist yet, the key value pair will be inserted

    hash_map[9] = 15

Deleting a key: use the del keyword. Key must exist or you will get an error.
    
    del hash_map[9]

Get size

    len(hash_map) # 3

Get keys: use `.keys()`. You can iterate over this using a for loop.

    keys = hash_map.keys()
    for key in keys:
        print(key)

Get values: use `.values()`. You can iterate over this using a for loop.

    values = hash_map.values()
    for val in values:
        print(val)

If you want to convert `my_dict.keys()` into a list, you would have to use `list(my_dict.keys())`

Use `.pop()` to remove a key-value pair and return the vlaue:

    removed_value = my_dict.pop("key to remove")


Use `my_dict.items()` to iterate over the key-value pairs of a dictionary:

    for my_key, my_value in my_dict.items():
        print(my_key, my_value)

If you only need to loop over only the keys:

    for my_key in my_dict:
        print(my_key)

Looking up a non-existing key returns a KeyError:

    filled_dict["four"]  # KeyError

Use "get()" method to avoid a KeyError, which supports a default argument when the value is missing:

    filled_dict.get("one")      # => 1
    filled_dict.get("four")     # => None
    filled_dict.get("one", 4)   # => 1
    filled_dict.get("four", 4)  # => 4




---

## **Loops**

Syntax | Meaning
--- | ---
`break` | A keyword that will exit an entire loop
`continue` | A keyword that will immediately advance one interation in a loop
`range(start, stop, step)` | creates a looping sequence wherein stop is exclusive

---

## **Variables and Mutability**

**Examples of mutation and modification include:**
- Appending or removing an item to a list
- Adding or removing a key-value pair to a dictionary

**Examples of operations that do *not* mutate or modify include:**
- Adding two numbers, resulting in a third number, such as `sum = 1 + 2`
- Incrementing a number stored in a variable, like `num += 1`

Remember that....**attempting to change (adding, multiplying, etc) an IMMUTABLE object actually just produces a different object with a different ID**

Whereas... **MUATBLE objects do not change object IDs when the object is modified or mutated.**

Together that means... **when you call a function, you pass a reference from the argument to the parameter, so they're both going to refer to the same object in memory. if it's a mutable object, like a list or dictionary, anything you do to the parameter, gets reflected back to the original argument.**

**Immutable**: Strings, Tuples
**Mutable**: Arrays, Hashes, Sets

---

## **Conditional Operators**

### `and`

For `and`, **if and only if both sides are truthy, then the entire expression is `True`. Otherwise, it's `False`.**
"Left" refers to what's on the left of the `and`, "Right" refers to what's on the right of `and`, and "Result" is what the expression evaluates to.

Left | Right |	Result
--- | --- | ---
True | True | True
True | False | False
False | True | False
False | False | False

### `or`

Expressions with an `or` evaluate to `True` when at least one side of the `or` is truthy.
(This explains the short-circuiting phenomenon in Python - if the interpreter finds the left side to be truthy, it will not go on to evaluate the right side). 

Left | Right |	Result
--- | --- | ---
True | True | True
True | False | True
False | True | True
False | False | False

### `not`

When `not` is in front of a truthy expression, the entire expression becomes `False`. When `not` is in front of a falsy expression, the entire expression becomes `True`.


## **Operator Precedence**

from highest (`()`) to lowest (`lambda`), wherein the highest-precedence operator will be evaluated first, and then on down the priorty line.

**Note this important ranking:**

relational operators > `not` > `and` > `or`

Operator | Meaning
--- | ---
`()`	| Parentheses (grouping)
`f(args...)`	| Function call
`x[index:index]`	| Slicing
`x[index]`	| Subscription
`x.attribute` | Attribute reference
`**`	| Exponentiation
`~x`	| Bitwise not
`+x, -x`	| Positive, negative
`*, /, %`	| Multiplication, division, remainder
`+, -`	| Addition, subtraction
`<<, >>`	| Bitwise shifts
`&`	| Bitwise AND
`^`	| Bitwise XOR
 &#124;  	| Bitwise OR
`in, not in, is, is not, <, <=,  >,  >=,<>, !=, ==`	| Relational operators: Comparisons, membership, identity
`not x`	| Boolean NOT
`and`	| Boolean AND
`or`	| Boolean OR
`lambda`	| Lambda expression

---

## Frequency Map Template

    def map_character_frequency(words):
        char_map = {}
        for word in words:
            for character in word:
                if character not in char_map:
                    char_map[character] = 1
                else:
                    char_map[character] += 1
        return char_map

---

## **Advanced Concepts**

Some notes on concepts that generally fall into the DSA bucket and are not exclusive to Python. The following have helped me assimilate some of the info above into a broader "algorithmic-thinking" context:

- Everytime a function is **called**, it is **pushed** onto the call stack. Everytime a function **returns**, it is **popped** off the call stack. Also, every function call stores its own variables.Helpful for navigating recursive patterns. 
- Drawing the call stack at each recursive step is helpful for understanding what's happening. Call stacks <-> recursion 
- DFS (depth-first search) is an example of an algorithm that's actually easier to implement and understand recursively. An iterative approach to DFS will likely still involve implementing your own stack, as opposed to the recursive approach which makes use of the Python interpreter's call stack.
- When writing a recursive function, it's sometimes helpful to first think of your func as a blackbox that just already does the thing you want it to do without worrying about how. THEN figure out the base case, and then figure out the rest of the implementation. 


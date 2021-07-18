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

## **Lists**


This is example syntax for modifying one element in a nested list.

    my_list[inner_list_index][element_index] = new_value


The `remove()` method will remove the **first instance** of a value in a list.

    list = [1, 2, 3, 1]
    list.remove(1) # Output: [2, 3, 1]

The `pop()` method removes an element at a given index, and will also return the removed item.

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

## **Dictionaries**

Use `.pop()` to remove a key-value pair and return the vlaue:

    removed_value = my_dict.pop("key to remove")


Use `my_dict.items()` to iterate over the key-value pairs of a dictionary:

    for my_key, my_value in my_dict.items():
        print(my_key, my_value)

If you only need to loop over only the keys:

    for my_key in my_dict:
        print(my_key)

**If you wanted to convert `my_dict.keys()` into a list, you would have to use `list(my_dict.keys())`**

    for my_key in my_dict.keys():
        print(my_key)

Use `my_dict.values()` for looping over only values:

    for my_value in my_dict.values():
        print(my_value)

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
[Markdown Syntax Guide](https://www.markdownguide.org/basic-syntax/)

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

Note this important ranking:
relationship operators > `not` > `and` > `or`

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
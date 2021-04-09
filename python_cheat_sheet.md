****# Python Syntax 

[Click for Markdown Guide](https://guides.github.com/features/mastering-markdown/)


## **Importing and Project Organization** (probably move this section into a new md file)
Syntax | Meaning
--- | ---
`from name_of_package.name_of_module import Class` | how to import a class, using the names of the module (just name of module, ommitt the .py) and package it lives in
`from .name_of_class_module import Class` | relative import 
`from name_of_class_module import Class` | absolute import 
`from name_of_module import *` | ?

## **OOP**

Syntax | Used To...
--- | ---
`self.attribute_name` | read an attribute inside of a class
`self.attribute_name = value_expression` |  write an attribute inside of a class and assigning a value to it
`ExampleClassName()` | create an instance of that class (assuming no required args)
`name_of_instance = ExampleClassName()` | create an instance of that class and stores it in a variable
`example_instance.name_of_attribute` | read an attribute from an instance 
`example_instance.attribute_name = new_attribute_value` | re-assign the value of attribute on an instance 
`self.name_of_instance_method` | call an instance method INSIDE a definition
`name_of_instance.name_of_instance_method()` | call an instance method OUTSIDE a definition
`super().parent_class_method() ` | general syntax for super() method
`super().__init__(arg1, arg2, etc)` | super refers to the parent class, and construtor of the parent class, and pulls those attributes (passed in as arguments) from the parent class and sets them up as attributes in the child class it's being called in 

`dir()` | list all of the methods that a particular class has (helpful for debugging)
`vars()` | makes a dictionary of an object's attributes (helpful for debugging)



## **Typical OOP-Related Errors**
Error | Meaning
--- | ---
`NameError: name 'ExampleClassName' is not defined` | This suggests that the class named `ExampleClassName` hasn't been defined before trying to instantiate it
`AttributeError: 'ExampleClassName' object has no attribute 'missing_attribute_name'` | suggests that we are trying to read an attribute from an instance of this class, but that attribute doesn't have a value
`TypeError: __init__() takes 0 positional arguments but 1 was given` | This suggests that the constructor doesn't define the first parameter `self`

## **Testing Objects**

    def test_some_example_test_case():
        # Arrange
        # Create an instance of the class
        # and set up any other necessary test variables

        # Act
        # Call the method that we are testing

        # Assert
        # Verify all relevant return values and state changes





## **Operator Precedence**
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
`in, not in, is, is not, <, <=,  >,  >=,<>, !=, ==`	| Comparisons, membership, identity
`not x`	| Boolean NOT
`and`	| Boolean AND
`or`	| Boolean OR
`lambda`	| Lambda expression
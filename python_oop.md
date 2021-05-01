[Markdown Syntax Guide](https://www.markdownguide.org/basic-syntax/)

---

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

---

## **Decorator Pattern Syntax (in Python)**

    def wrapper_function(wrapped_func):
        def inner():

            # some wrapper logic

            wrapped_func()

            # some wrapper logic

        return inner

    @wrapper_function
    def wrapped_function():
        # replace pass with whatever function logic
        pass

---

## **Static Methods Syntax**

    class ExampleClass:    

        @staticmethod
        def example_method():
            print("I'm inside the static method, example_method!")

## **Class Methods Syntax**

    class ExampleClass:    

        @classmethod
        def example_method(cls):
            print("I'm inside the class method, example_method!")
            print("In a class method, cls will be the class itself", cls)


## **Comparing Python Methods: Instance, Class, Static**

Method | Parameter | Decorator | Accessing
--- | --- | --- | ---
Instance Method (Most Common) | must have `self` parameter | no decorator needed | can be accessed through object (instance of Class) 
Class Method | doesn't need `self`, but does need `cls` parameter | needs decorator `@classmethod` | can be accessed directly through class; doesn't need instance of class
Static Method | doesn't need `self` or `cls` parameter | needs decorator `@staticmethod` | can only access variables passed as argument; a static method cannot be accessed through class or its instance
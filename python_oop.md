[Markdown Syntax Guide](https://www.markdownguide.org/basic-syntax/)
---

## **OOP Concepts**

- Instance methods are behaviors instances can do
- Instances of a class do not share state, but they do share behavior. Each instance of a class has its own state

---

## **OOP Summary Syntax**

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
## **OOP Relationships**

- Inheritance = passing on implementation
- Composition = instances holding instances

### **Syntax for inheritance**:

    class ExampleChildClass(ExampleParentClass):
        pass


If a child class needs to *replace* the implementation of an inherited method, the child class can *override* the method by redefining it with the same name:

    class ExampleParentClass:
        def example_instance_method(self):
            print("I'm inside of ExampleParentClass!")

    class ExampleChildClass(ExampleParentClass):
        def example_instance_method(self):
            print("I'm inside of ExampleChildClass!")



Calling `super()` returns a temporary object of the parent class (also known as the superclass!). With this superclass, we can call all of the superclass's methods.

    class Adult:
        def make_phone_call(self):
            print("I'm picking up the phone and dialing a number and using my voice!")

    class Texter(Adult):
        def make_phone_call(self):
            print("I'm waiting four days")
            print("Now I'll forget to call them back")
            print("Now I'm just texting them instead")
        def make_emergency_phone_call(self):
            super().make_phone_call()

    terry = Texter()
    terry.make_phone_call()
    terry.make_emergency_phone_call()

The above code outputs:

    I'm waiting four days
    Now I'll forget to call them back
    Now I'm just texting them instead
    I'm picking up the phone and dialing a number and using my voice!

### **Syntax for Composition**

A **one-to-one relationship** is a relationship in which a composite class has an attribute representing a single instance of a component class

    class ExampleComponent:
        def __init__(self, name):
            self.name = name
    class ExampleComposite:
        def __init__(self, name, component):
            self.name = name
            self.component = component

A **one-to-many relationship** is a relationship in which a composite class has an attribute representing a **list** of instances of a component class

    class ExampleComposite:
        def __init__(self, name, components):
            self.name = name
            self.components = components # components is a list of component objects!


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

## **Instance Method Syntax**

    class ExampleClassName:

        def example_instance_method(self):
            pass

## **Static Method Syntax**

    class ExampleClass:    

        @staticmethod
        def example_method():
            print("I'm inside the static method, example_method!")

## **Class Method Syntax**

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
## **Reading the Stack Trace**

As a general rule, the ultimate error is listed at the bottom, and line of code that raised that error is at the bottom.It is helpful to read the stack trace from the bottom, going up.

Example: 

Traceback (most recent call last): 
   File "main.py", line 5, in <module>
      apple_basket_quantity = number_of_apples / basket_capacity 
ZeroDivisionError: division by zero

1. The description of the error is `division by zero`
2. The name of the error is `ZeroDivisionError`
3. The line of code that caused the error is in `main.py` on line 5

## **Configuring Pytest from VS Code (one-time set up)**

**You will need to configure the tests (i.e. complete the following steps) for every new project!!!!**

1. CMD SHIFT P to open command pallete
2. Select 'Python: Configure Tests'
3. Select pytest
4. Select directory containing test files
5. From the Test Explorer:
    - Can run all tests (arrow at top, next to Test Explorer)
    - Can run just one test file (green arrow next to test file name)
    - Can run a single test within a file (expand that test file, then green arrow next to text)


## **Reading Pytest results**

`pytest` has a rule about naming individual tests: It will only recognize test names begin with `test_` or end with `_test`. 

1. `test session starts` will print some facts about the tests, like how many tests there are. There will be a series of `.`s for passing tests, and `F` for failing tests.
2. `FAILURES` will print any tests that failed, the names of the test and what file and line it's on, and how these tests failed.
3. `short test summary info` will print a short test summary info, including overall how many tests passed or failed, and how long the tests took to run.

## **Anatomy Of A Pytest**

    def test_some_example_test_case():
        # Arrange
        # Create an instance of the class
        # and set up any other necessary test variables

        # Act
        # Call the method that we are testing

        # Assert
        # Verify all relevant return values and state changes

---

## **Debugging tricks**

### Breakpoints
A **breakpoint** is a place (line of code) which indicates to the debugger to pause the program at this point of execution. While the program is paused, the dev running the debugger can examine the state of variables currently in scope. After that, the dev can resume execution or execute the program, line-by-line.

### Watches
Sometimes we need to track the value of an expression that is never stored in a variable. We can supply the debugger tool with expressions to watch. The debugger lists and shows the current value of each watched expression through the entire program execution.

## **Debugging with Breakpoints - Example Workflow**

1. Put a breakpoint at the line of code that is causing the program to crash
2. Go to debugger
3. You may need to click on the select list, select Add Configuration and choose select Python: Current File. You may need to click on the select list, select Add Configuration and choose select Python: Current File.
4. Run the debugger by pressing green triangle "play" button

## **Debugging a Failing Test - Example Workflow**


1. Run the tests from the test explorer
2. Find the .py file of the failing test
3. Now you have two options:
   1. Create a breakpoint in the failing test and use the step-into and step over commands to trace through the code and see why the test is failing
   2. Select the Debug Test link above the test function to run that one test in the debugger.


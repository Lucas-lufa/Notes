Two Week
 mkdir temp && cd temp
 <program> --version
 cat concatonates everything together and send to standard output
 .gitattrubtues is a path-specific setting file.
## module
 import file
 import file as f # alias a file as f
 from file import something # from a file import something like a class or function
 when a python file is run it is given the __main__ of "__main__" if a module is run __main__ is it's file name ie the module is greet __main__ will be "greet"
 if name == "__main__":
    main()
 main() runs what is put into to in, useally all the functions want to text.
## pass by reference

## In-class revision
 At the end of this class, you should be able to answer the following questions:

 What is a module in Python? How do you create one?
 What is the purpose of the import statement in Python? Can you provide a code example of its usage?
 How can you import only a specific function or class from a module in Python? What is the syntax for this?
 How would you explain Python's parameter-passing mechanism? Is it more similar to pass-by-value or pass-by-reference?
 Given the following Python code, what will be the output and why?
 def modify_list(lst):
    lst.append("new")
    lst = ["completely", "new"]

 items = ["original"]
 modify_list(items)
 print(items)
 If Python uses pass-by-reference, why does not reassigning a variable inside a function change the original variable outside the function? How is this related to the mutability of Python objects?

One Week
https://realpython.com/list-comprehension-python/
# turnery expression
# list comprehension
## new_list = [expression for member in iterable]
 expression is the member it self, method call or any 
expression that returns a value.
 member is the object or value in a list.
 iterable is a list, set, generator or any other object that can return it's values one at a time.

## list comprehension can also be used for mapping and filtering
 Look filter() and map()

## new_list = [expression for member in iterable (if conditional)]
 The conditional in not in parentheses when writing code. 
 The conditional in this case is at the end. 
 conditional is important because it allows list comprehension to filter out values.
 The conditional can test any valid expression - if more complex filtering can move the conditional logic to a separate function.

## new_list = [expression (if conditional) for member in iterable]
 If you want to change the member item instead of filtering it out, the conditional needs to be at the front of the expression.
 With this formula it is possible to select one of multiple possible values.

# Walrus operator or assignment operator
## need more info
 Allows to run an expression and simultaneously assignment it's output to a variable

# set comprehension 
 like list comprehension but with braces {} instead brackets []

# dictionary comprehension
## new_dictionary = { key : values expression for member in iterable}  
 To create a dictionary use braces () and a key value pair in the member


Two Week
 mkdir temp && cd temp
 <program> --version
 cat concatenates everything together and send to standard output
 .gitattrubtues is a path-specific setting file.
## module
 import file
 import file as f # alias a file as f
 from file import something # from a file import something like a class or function
 when a python file is run it is given the __main__ of "__main__" if a module is run __main__ is it's file name ie the module is greet __main__ will be "greet"
 if name == "__main__":
    main()
 main() runs what is put into to in, usually all the functions want to text.
## pass by reference
>>> def modify(n, list_):
...    n = 2
...    list_.append(3)
...    print(f"n modify{id(n)}")
...    print(f" list modify{id(list_)}")
... 
>>> n = 1
>>> list_ = [1, 2]
>>> print(f"n {id(n)}")
n 140284462629104
>>> print(f" list {id(list_)}")
 list 140284461388416
>>> modify(n, list_)
n modify140284462629136
 list modify140284461388416
>>> print(n) # Outputs: 1
1
>>> print(list_) # Outputs: [1, 2, 3]
[1, 2, 3]

 When a mutable object is pass into function it is passed by reference, when the function ends the is still a reference to it. When amn immutable object is passed into the function it is copied in and a new reference is made, when the function ends so dose the new reference.

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

# Python in a nutshell
https://learning.oreilly.com/library/view/python-in-a/9781098113544/ch03.html#:-:text=Object%20attributes%20and%20ite,ms
 Object attributes and items

The main distinction between the attributes and items of an object is in the syntax you use to access them. To denote an attribute of an object, use a reference to the object, followed by a period (.), followed by an identifier known as the attribute name. For example, x.y refers to one of the attributes of the object bound to name x; specifically, that attribute whose name is 'y'.

To denote an item of an object, use a reference to the object, followed by an expression within brackets []. The expression in brackets is known as the item’s index or key, and the object is known as the item’s container. For example, x[y] refers to the item at the key or index bound to name y, within the container object bound to name x.

Attributes that are callable are also known as methods. Python draws no strong distinctions between callable and noncallable attributes, as some other languages do. All general rules about attributes also apply to callable attributes (methods).

https://learning.oreilly.com/library/view/python-in-a/9781098113544/ch03.html#:-:text=Each%20of%20these,as%20extended%20unpacking.
extended unpacking
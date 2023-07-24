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


# turnery expression
# list comprehension
new_list = [expression for member in iterable]
 expression is the member it self, method call or any 
expression that returns a value.
 member is the object or value in a list.
 iterable is a list, set, generator or any other object that can return it's values one at a time.
## list comprehension can also be used for mapping and filtering
new_list = [expression for member in iterable (if conditional)]
 conditional is important because it allows list comprehension to filter out values.

# dictionary comprehension
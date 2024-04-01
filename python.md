### python general

https://docs.python.org/3/using/cmdline.html
python can be run as a -c command -m module or a script

### sphinx
setup virtual environment
python3 -m venv .venv
install from pypi
pip install -U sphinx
pip install sphinx_rtd_theme

install miniconda
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

~/miniconda3/bin/conda init bash

source ~/miniconda3/bin/activate

conda env create -f https://raw.githubusercontent.com/coderefinery/software/main/environment.ym

Make sure that you see “coderefinery” in the output when you ask for a list of all available enviro

conda env list

conda activate coderefinery
conda deactivate
conda remove --name coderefinery --all

Sphinx and markdown

conda activate coderefinery

check we have the software needed
python --version
sphinx-build --version
sphinx-quickstart --version
python -c "import myst_parser" (you should see no output)
I needed to install with one of these methods (think used pip)
conda install -c conda-forge myst-parser
pip install myst-parser

 sphinx quick start
The example make a directory step into it and run the sphinx quick start to generate basic documentation template:
mkdir doc-example
cd doc-example
sphinx-quickstart

for me. run in sphinx_activity directory # This was a mistake. Think needs to be in a sub folder, otherwise will look in folders you don't want like venv

I put all my markdown into a docs folder and run sphinx-quickstart in there.

The quick start utility will ask you some questions. 
Separate source and build directories (y/n) [n]: default hit enter
Project name: your project name
Author name(s): your name
Project release []: 0.1
Project language [em]: default hit enter

files and directories are created:
conf.py Documentation configuration file
index.rst Main file in sphinx
_build/ Directory where docs are built (you can decide the name)
_templates/ Your own HTML templates
_static/ Static files (images, styles, etc) copied to output directory on build
Makefile Makefile to build documentation using make
make.bat Makefile to build documentation using make (windows)

look at index.rst
remove indices and tables down. add what want to document
example 
some-feature.md
indented the same as above and a line between(inline with :caption: Contents:)
me
   :caption: Contents:

   some_feature.md
   another_feature.md
   api.md
can't add python scripts until autodocs
example.py
tic_tac_bug_toe.py
indented the same as above (inline with :caption: Contents:)

look at conf.py
put 'myst_parser' into extensions list

example create some-feature.md file referenced in index.rst

We now build the site:
ls -1 (1 flag put each entry on it's own line)
sphinx-build . _build (builds this directory into the _build directory)
then open _build/index.html in a browser.
this works for markdown but so far not python files

 Adding more sphinx content
made another-feature.md file and referenced in index.rst

 sphinx and latex math equations

### sphinx autodoc
auto-generating documentation from Python docstrings

make python modules example with docstrings
make a api.md with content.
 API reference

  example

```{eval-rst}
.. automodule:: example
   :members:
```

add three lines to conf.py
import os
import sys
sys.path.insert(0, os.path.abspath("."))
modify extensions add 'spinx.ext.autodoc' to the list

sphinx-build looks in index.rst for markdown files need to make static site from. the api.md has in it a reference to pythons scripts need to document. And the conf.py by importing modules so it can set path and adding extentions. Allows sphinx to read docstrings in python scripts

 good to know
_build directory is a generated directory and should not be part of git repository.
sphinx-autobuild provides a local web host that automatically refresh your view every time save a file.
sphinx-build . -W -b linkcheck _build

### decision to leave

### testing and documentation techniques
raise issue
create local branch
create a test case that fails, create a pull Request

fix

pass test case


Five Week
 ### Q
 is encoding or interpretation why we have types and type errors?
 slide 17 why is it important that it is a static method or not?

 ### link
 wave - sound
 https://docs.python.org/3/library/wave.html
 sqlite3
 https://docs.python.org/3/library/sqlite3.html
 socket
 https://docs.python.org/3/library/socket.html
 struct
 https://docs.python.org/3/library/struct.html
 pillow
 https://pypi.org/project/Pillow/
 OpenCV
 https://pypi.org/project/opencv-python/

 ## Binary files have high-level interface:
 Just as utf-8 is a high-level interface for text. Most binary files also have high-level interfaces.
 wave - to work with WAV sound files.
 sqlite3 - work with sqlite database files, to access and manipulate the binary data.
 socket - facilitates network communications
 struct - converts between python values and c structs represented as python bytes objects.
 pillow - pil python imaging library 
 openCV - computer vision

 bitwise
 
 pptx
 binary files, formats and access

 ## Scenario
 Consider the following fictional image file format:
File Structure: A binary file containing image data.
First 9 bytes: Text encoded with the dimensions of the image (e.g., "1920x1080").
Following bytes: Series of 3 bytes representing RGB values of each of the pixels.
E,g. 1920x1080200244002

### questions
Given the specification, outline how you would use seek, read, write, and tell (as appropriate) to:
(a) Retrieve the RGB Value of the Center Pixel
( b) Retrieve all pixel values as integers from a random 100x100 grid within the image
(b) Reduce the resolution by half

 ## What Are Random-Access Algorithms?
Random-access algorithms allow data to be read or written in any order, as opposed to sequential access, where data must be accessed in a specific sequence. Random access enables programs to jump directly to a specific location within a file, making it ideal for binary file handling where data might be scattered or organized in non-sequential blocks.
Importance in Binary File Handling
When working with binary files, data is often organized in complex structures, and direct access to specific parts is crucial. Random-access algorithms enable the efficient management, retrieval, and modification of specific portions of data without having to traverse the entire file.

Seeking: This is the act of moving the file position pointer to a specific location in a file.
Reading and Writing: With the position pointer at the desired location, data can be read or written at that spot.
Tell: This function allows you to find the current position of the file pointer.

 ## What is a byte object
 representation of a sequence of bytes,
 iterable (like a list or tuple),
 each element is of type integer 0-255

 .encode() text -> binary
 .decode() binary -> text

 ().to_bytes() int -> binary, the front parentheses has the integer and the parameter parentheses tells the length of bytes to put the output in. If the output is bigger than the byte assigned will raise an OverflowError.
 int.from_bytes(bytes to convert to integer) it is a static method.

 ## binary file handling
 Binary modes behave similarly to their text counterparts but operate on the file as raw bytes rather than handling the content as encoded characters. This makes binary modes suitable for non-text files like images of any situation where precise byte-for-byte handling is required.

 We open a file in binary when we don't want to interpret the file and instead we intent on getting the value of each eight bits(usually represented as a decimal 0-255)

 "br" bunny rabbit, read only binary mode. File must exist, on open starts at the beginning of the file. Can read but can't write.
 "br+" Read and write binary mode. Same as 'br' but can write as well as read.
 "wb" White bunny, write only binary mode. Truncates if exists or creates a new file. Starts from the beginning of a file.
 "wb+" Same as 'wb' but reads and writes.
 "ab" Appends if file exist or creates a new file. Starts at the end of a file, can write.
 "ab+" Same as 'ab' but can read and write.
 
 ## file handling
 "r" Must exist, reads the file from pointer onwards. On opening a file pointer is at the beginning but can be moved. Can't write.
 "r+" same as 'r' but can write as well.
 "w" starts at the beginning. It truncates or creates a new file if doesn't exist, can write can't read.
 "w+" same as 'w' but can read as well.
 "a" appends starts at the end of a file. Appends to a file or creates a new one if doesn't exist. Can write can't read.
 "a+" dose the same as append but can read as well as write.
 
ipos 5 session
```python
'''Revision on reading and writing text files in Python 
With a twist: what happens when we use multi-byte characters?
How do we move backwards in the file?'''

# Create the file we will work with, try:
# remove encoding and see what happens
# remove encoding and the emojis and see what happens
with open("my_new_file", "w", encoding='utf-8') as f:
    f.write("Hello😊😊\nWorld")

# Ditto: try removing encoding and see what happens    
with open("my_new_file", "r", encoding='utf-8') as f:
    print(f.read()) # prints the content

   Hello😊😊 
   World 

    print(f.read()) # prints nothing, why?
    # read() moves the pointer to the end of the file while reading.
    # move the cursor back to the beginning of the file
    f.seek(0)
0
    print(f.read()) # prints the content again
    f.seek(0)
0
    for _ in range(5):
        print(f.read(1)) # prints the first 5 characters
H
e
l
l
o
    print(f.tell()) # tells us where the cursor is.
5
    # At index five where the for loop places it.
    print(f.read(1)) # prints the emoji, I 
😊
    print(f.tell()) # tells us where the cursor is - WHAT? Notice where the cursor is, it jumped 4 bytes!  # noqa: E501
9
    # if you have removed the encoding, see what happens here and continue reading - notice no emoji just 4 random characters # noqa: E501
```

Four Week
 unittests
 https://realpython.com/python-assert-statement/
 Python in a Nutshell, 4th Edition
 Chapter 17. Testing, Debugging, and Optimizing
 https://learning.oreilly.com/library/view/python-in-a/9781098113544/ch17.html

Three Week
 unittests

 2d data
 list comprehension or two for loops nested

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
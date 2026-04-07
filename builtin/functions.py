# Review of functions from Chapter 4

# All import statements should be near the top of a .py file.
# If we need to know what packages a .py file needs, we don't
# want to scroll through many lines of code to find them.
# This line imports the 'sqrt' function from the 'math' package.
# The 'math' package is builtin. We don't need to install it.

from math import sqrt

# All global constants should be near the top of a .py file.
# Variables defined outside all functions (and classes) are
# called "globals." Any code in this .py file can use them.
# Python doesn't really have constants, but we do have a
# convention: if a variable name is CAPITALIZED, it means
# "I'm using this as a constant. Please do not mutate it."

PLANET = "地球"

def hello():
    # Print three greetings.
    # I copypasted this function from page 73, then changed it.
    print("早上好")
    print("下午好")
    print("晚上好")

hello()

def say_hello_to(name):
    # Print three greetings to the name provided.
    # I copypasted this function from page 75, then changed it.
    print("早上好 " + name)
    print("下午好 " + name)
    print("晚上好 " + name)

say_hello_to("Ada Lovelace")
say_hello_to("Charles Babbage")

def mean(x, y):
    # Average of two numbers.
    # This function inputs two args and returns one output.
    return (x + y) / 2

for x in range(10):
    print("The mean of 0 and", x, "is", mean(1, x))

# I did not tell Python what type x and y should be.
# Python doesn't check argument types. Floats also work:
print("The mean of 0 and 0.1 is", mean(0, 0.1))
print("The mean of 1.5 and 2.5 is", mean(1.5, 2.5))

# If we input the wrong types, Python will still try to call the
# mean() function. It will raise an error and crash.
# print("The mean of '一' and '三' is", mean("一", "三"))

# Python functions always return something.
# If we write a function with no 'return' statement,
# then Python will assume we meant 'return None'.
spam = mean(0, 100)
print("mean(0, 100) returned", spam)
spam = hello()
print("hello() returned", spam)

# None is a special object with its own type.
# None is often used as a 'null value' in Python.
# In files and databases, null values indicate "我们不知道".
# Null values are important in NumPy, SQL, Spark, etc.
print("type(None) is", type(None))

# We can define functions with an unknown number of args:

def say_hello_to_all(*args):
    # Print three greetings to the names provided.
    for name in args:
        print("早上好 " + name)
        print("下午好 " + name)
        print("晚上好 " + name)

say_hello_to_all("Ada", "Charles", "Guido", "Sam")

# Functions can also accept 'named parameters' as input.
# These are also called 'keyword arguments' or 'kwargs'.
# Kwargs are often used for optional inputs.
# In this example, 'name' is a kwarg with default value None.

def say_goodbye(name=None):
    # Print a goodbye message to the name provided.
    # If no name is input, print a generic goodbye.
    if name is None:
        print("再见")
    else:
        print("再见" + name)

say_goodbye(name="Ada Lovelace")
say_goodbye(name="Charles Babbage")
say_goodbye()

# Many builtin functions accept kwargs. For example, print()
# accepts a kwarg called 'sep'. It means 'separator'.
# If you call print multiple args, Python inserts a separator
# between them. The default value of 'sep' is a space.
print("Ada", "Charles", "Guido")
print("Ada", "Charles", "Guido", sep=" & ")

# SUPER BONUS PROBLEM FOR BORED PEOPLE
# What does this function do? Why would anyone do this?

def show_kwargs(**kwargs):
    # ??? useless mystery function ???
    print("type(kwargs) is", type(kwargs))
    for key, value in kwargs.items():
        print(key, ":", value)

show_kwargs(teacher="Ada", student="Sam")

# If we define a variable inside a function, then that variable
# only exists inside that function. This is called "scope."
# In the previous example, I defined 'name' inside say_goodbye().
# For any code outside say_goodbye(), 'name' is out of scope.
say_goodbye(name="Sam")
try:
    print(name)
except NameError as err:
    print("Error!", err)

# Programmers use scope to prevent our functions from reading
# or mutating variables inside other functions.
# The 'location' variable in a function is not the same as
# the 'location' variable in any other function.

def i_am_from(location):
    # Tell people where I come from.
    print("我是", PLANET, location, "人", sep="")


def i_am_in(location):
    # Tell people where I am now.
    print("我在", PLANET, location, sep="")

i_am_from("美国")
i_am_in("中国")

# Functional programmers like simple functions that do one thing
# well. For complicated tasks, they write functions that call
# other functions. This is called "composition."

def euclid(*args):
    # Given a vector's components, find its Euclidean norm.
    return sqrt(sum(x * x for x in args))

print("The Eucliean norm of (3, 4) is", euclid(3, 4))
print("The Euclidean norm of (1, 2, 3) is", euclid(1, 2, 3))

# Review of lists, tuples, and sets.

import random

# This uses Python builtins. You don't need .venv or Jupyter.
# If you don't have a working .venv or Jupyter, that's OK!
# We'll have time later in class to fix those things.

# ADVANCED TOPIC FOR BORED PEOPLE:
# If you already know list indexing, slicing, and comprehensions,
# and your .venv and Jupyter setup works, do this:
# 0. Create a new notebook called arrays.ipynb.
# 1. Type this line in the first cell: import numpy as np
# 2. Try to do these examples with np.array() instead of list().
# The docs are here (and in the syllabus, and in README.md):
# https://numpy.org/doc/stable/user/absolute_beginners.html

# Here are some example lists:
empty = []
names = ["Ada", "Charles", "Grace", "Guido", "Linus", "Sam"]
scores = [100, 90, 98, 80, 0, 42]

# Class assigment: list the names in your group.
# Use 汉字 if you want to. Python doesn't care!
# Any sequence of valid Unicode characters can be a string.
# Whatever I do with my 'names' variable, try it with yours.

# The builtin len() function returns list length.
print("list lengths are", len(empty), len(names), len(scores))

# List "indexes" are numbers starting from 0.
# We can use them to get one element from a list:
print("names 0, 1, 2 are", names[0], names[1], names[2])

# Index backwards using negative indexes:
print("names -1, -2, -3 are", names[-1], names[-2], names[-3])

# If you use an impossible index, Python will crash:
try:
    names[100]
except IndexError as err:
    print("Error!", err)

# We can get multiple elements by "slicing."
# Slices accept (start, stop, step) args.
print("names[0 : 2]", names[0:2])
print("names[2 : -1]", names[2:-1])
print("names[0 : -1 : 2]", names[0:-1:2])

# We can make lists of almost any object.
# This example is a list of lists.
exam = [names, scores]
print("grades", exam)
print("grades[0]", exam[0])
print("grades[0][0]", exam[0][0])
print("grades[0][1]", exam[0][1])
print("grades[0][2]", exam[0][2])

# Length, index, and slicing also work on strings.
my_name = "Sam"
print("len(my_name)", len(my_name))
print("my_name[0]", my_name[0])
print("my_name[-1]", my_name[-1])
print("my_name[0 : 2]", my_name[0:2])

# Lists are "mutable." We can change values:
names[-1] = "Samuel"
print(names)

# We can add and remove elements:
names.append("Max")
print(names)
names.remove("Max")
print(names)

# The + and * operators also work on lists.
print(names + ["Valtteri", "Checo"])
print(names * 2)

# Lists and strings are "iterable."
# That means they have a hidden .__iter__() method.
# That means we can "iterate over them" with for loops.
for name in names:
    print(name)

# Use enumerate() to loop over indices and values.
for i, name in enumerate(names):
    print("Student number", i, "is named", name)

# We can make new lists by iterating over lists.
low_names = []  # [ ] means "empty list"
for name in names:
    low_names.append(name.lower())
print("Lowercase names:", low_names)

# Python has a special syntax for looping over iterables.
# This is called a "list comprehension."
low_names = [x.lower() for x in names]
print("Lowercase names:", low_names)

# This list comprehension converts ints -> floats.
p_scores = [x / 100 for x in scores]
print("Score %", p_scores)

# Python doesn't check types when you iterate.
try:
    [x.lower() for x in scores]
except AttributeError as err:
    print("Error!", err)

# The 'in' operator returns a bool (True or False).
print("Is 'Sam' in names?", "Sam" in names)
print("Is 'Samuel' in names?", "Samuel" in names)

if ("Sam" in names) or ("Samuel" in names):
    print("Sam is here")

if "Dave" not in names:
    print("Dave is not here")

# List comprehensions can include conditions.
# This is called "filtering" a list.
g_names = [x for x in names if x.startswith("G")]
print("Names that start with G:", g_names)

# This list comprehension uses 'not in' to filter a list.
bad_names = ["Linus", "Sam", "Samuel"]
best_names = [x for x in names if x not in bad_names]
print("Best students:", best_names)

# zip() is used to loop over multiple lists together.
for name, score in zip(names, scores):
    print(name, "got", score, "points")

# We can make complex loops with iterators and comparisons:
for name, score in zip(names, scores):
    if name in bad_names:
        print(name, "must take the test again.")
    elif score == 100:
        print(name, "should be in a more advanced class.")
    else:
        print(name, "got", score, "points")

# random.shuffle() changes the order of values in a list.
random.shuffle(names)
print("Shuffled names:", names)
print("Samuel is student number", names.index("Samuel"))

# sorted() returns a sorted list
names = sorted(names)
print("Sorted names:", names)
print("Samuel is student number", names.index("Samuel"))

# Tuples are just like lists, but they're immutable.
# Tuples cannot be modified after they are created.
# Tuples can be created with tuple() or () instead of [].
bikes = ("Ducati", "Yamaha", "ZXMoto")
try:
    bikes[-1] = "BMW"
except TypeError as err:
    print("Error:", err)

# Sets are like mathematical sets.
# Sets can be created with the set() function or with { }.
cars = {"BMW", "BYD", "Ferrari", "Xiaomi"}
phones = {"Apple", "Google", "Huawei", "Xiaomi"}

# Try some set unions and intersections:
print("cars | phones:", cars | phones)
print("cars & phones:", cars & phones)

# No element can appear in a set more than once.
print("set([1, 0, 1]):", set([1, 0, 1]))

# Sets are mutable.
phones.add("Lenovo")
phones.remove("Google")
print(phones)

# frozenset() makes immutable sets.
frozen_phones = frozenset(phones)
try:
    frozen_phones.add("Google")
except AttributeError as err:
    print("Error!", err)

# Sets and frozensets are iterable like tuples and lists.
print("Lowercase phones:", {x.lower() for x in phones})

# Sets do not have a fixed order. They can't be indexed.
try:
    print(phones[0])
except TypeError as err:
    print("Error!", err)

# I often use set() and sorted() to do database tricks.
# In SQL, "SELECT DISTINCT" drops duplicated values.
cities = [
    "New York",
    "New York",
    "Chicago",
    "New York",
    "Philadelphia",
    "New York",
    "Chengdu",
    "New York",
    "New York",
    "New York",
]
print("Distinct cities:", list(set(cities)))

# In SQL, "ORDER BY" sorts values.
print("Sorted distinct cities:", sorted(set(cities)))

# By default, sorted() returns "lexsorted" values.
# "Lex" is short for "Lexicographic order."
# It's like alphabetic order with extra rules
# for numbers, different alphabets, and special characters.
words = ["成都", "北京", "Chicago", "Linus", "ZXMoto", "?"]
print("Sorted words:", sorted(words))
numbers = (2, 0, 0, 6, 0, 4, 0, 8)
print("Sorted numbers:", sorted(numbers))

# We can also pass a function to sorted() as a kwarg.
# It will use that function to compare elements.
print("Words sorted by length", sorted(words, key=len))

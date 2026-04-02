"""
Review of flow control from Chapter 2.
This chapter uses Booleans. Many of us call them "bools".
A bool can be True or False. It can't have any other value.
"""

## Comparisons


# (x == y) works a bit like 是不是.
# It is True if x and y have equal values.
# It is False if x and y do not have equal values.

print("14 == 14", 14 == 14)
print("14 == 40", 14 == 40)
print("'十四' 是不是 '十四'", "十四" == "十四")
print("'十四' 是不是 '四十'", "十四" == "四十")


# Be careful when comparing different types.
# 14 is an integer. "14" is a string.

print("14 == '14'", 14 == "14")
print("14 == '十四'", 14 == "十四")


# Strings are equal if every character is exactly the same.
# Capitalization matters! "Python" does not equal "python".

print("'Sam' == 'Sam'", "Sam" == "Sam")
print("'Sam' == 'sam'", "Sam" == "sam")
print("'Sam' == 'Samuel'", "Sam" == "Samuel")


## Logic operators


# (x and y) examples

print("(True and True) is", True and True)
print("(True and False) is", True and False)
print("(False and True) is", False and True)
print("(False and False) is", False and False)


# (x or y) examples

print("(True or True) is", True or True)
print("(True or False) is", True or False)
print("(False or True) is", False or True)
print("(False or False) is", False or False)


## Negations


# (not x) is the opposite of x's truth value.

print("(not True) is", not True)
print("(not False) is", not False)


# (x != y) is another way to write "x does not equal y"

print("14 != 14", 14 != 14)
print("14 != 44", 14 != 44)


## Using conditions to control programs


# 'if' statements are common in many languages.

if (14 != 40) and (40 == 40):
    print("十四不是四十。四十是四十。")


# 'else' tells Python what to do if the first condition is False.
# Caution: Don't write passwords in source code! It's unsafe.
# This is not my real password. I only use it for examples.

name = input("What is your name? ")
password = input("What is your password? ")
if (name == "Sam") and (password == "huajiao"):
    print("Hello, teacher!")
else:
    print("Access denied.")


# We can use 'elif' for multiple conditions.
# (In some languages, 'elif' is written 'else if'.)

language = input("What language should we speak? ")
if language == "English":
    print("Hello, World!")
elif language == "Deutsch":
    print("Guten Tag, Welt!")
elif language == "中文":
    print("你好世界！")
else:
    print("I'm sorry. I can't speak", language)


## Truthy and Falsey values


# Python can convert many types of values into bools.
# Values which are logically True are called "truthy".
# Values which are logically False are called "falsey".

print("bool(0)", bool(0))
print("bool(1)", bool(1))
print("bool('')", bool(""))
print("bool('Sam')", bool("Sam"))


# We can do logical comparisons with things that are not bools.
# Sometimes this is a bad idea. It can be very confusing.

print("not 1", not 1)
print("14 or 44", 14 or 0)
print("'Sam' and 'Linus'", "Sam" and "Linus")
print("not not not not 42", not not not not 42)

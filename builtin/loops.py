"""
Review of loops from Chapter 3.
"""

## while loops


# I copypasted this example from page 50 in the textbook.

spam = 0
while spam < 5:
    print("Hello, world!")
    spam = spam + 1


# This is an "infinite" loop. If the user does not give the
# answer we want, then it will loop again and again until
# the program crashes or you force it to stop with CTRL-C.

while True:
    answer = input("What is your favorite language? ")
    if answer != "Python":
        print("I don't like", answer, ". Try again.")
    else:
        print("Python is my favorite language too!")
        break


# This loop is an example of the 'continue' statement.
# Caution: Don't write passwords in source code! It's not safe.
# This is a fake password that I only use for code examples.

while True:

    name = input("What is your name? ")
    if name != "Sam":
        continue

    password = input("What is your password? ")
    if password == "huajiao":
        print("你好老师")
        break

    print("Access denied. Try again.")


# This loop uses "truthy" and "falsey" values.
# An empty string is falsey. All other strings are truthy.
# This will loop until the user types an answer.

answer = ""
while not answer:
    answer = input("What is your favorite color? ")


## for loops


# Here are two loops that do the same thing.
# I prefer the "for loop" because I don't need to type 'x += 1'.
# (If I forget that line, then the while loop will be infinite!)

x = 1
while x < 4:
    print("This loop ran", x, "times.")
    x += 1

for x in range(1, 4):
    print("This loop ran", x, "times.")


# range() is a builtin function. It comes with Python 3.
# It's useful for writing loops. Here are more examples:

print("Loop over range(4)")
for x in range(4):
    print(x)

print("Loop over range(1, 4)")
for x in range(1, 4):
    print(x)

print("Loop over range(4, 0, -1)")
for x in range(4, 1, -1):
    print(x)

print("Loop over range(0, 100, 10)")
for x in range(0, 100, 10):
    print(x)


# Another example of 'break' and 'continue' statements.
# This is like our previous name & password loop, but
# it's not an infinite loop. After 3 failed attempts,
# it will force the program to quit.

attempts = 3
for x in range(attempts, 0, -1):
    print(x, "attempts remaining.")

    name = input("What is your name? ")
    if name != "Sam":
        continue

    password = input("What is your password? ")
    if password == "huajiao":
        print("你好老师")
        break

if not attempts:
    print("Access denied.")
    import sys

    sys.exit()


# Python can loop over any 'iterable' object.
# Strings are iterable! Try looping over a string:

for char in "一二三四五六七 我的朋友在哪里？":
    print(char)

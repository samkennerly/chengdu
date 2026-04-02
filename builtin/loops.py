"""
Review of loops from Chapter 3.
"""

# while loops

# I copypasted this example from page 50 in the textbook.
# It's legal because it's open-source!
spam = 0
while spam < 5:
    print("Hello, world!")
    spam = spam + 1

# This is an "infinite" loop. If the user does not give the
# answer we expect, then it will loop again and again until
# the program crashes or you force it to stop with CTRL-C.
while True:
    answer = input("What is your favorite language? ")
    if answer != "Python":
        print("I don't like", answer, ". Try again.")
    else:
        print("Python is my favorite language too!")
        break

# An example of the 'continue' statement.
# Caution: Don't write passwords in source code! It's unsafe.
# This is not my real password. I only use it for examples.
while True:

    name = input("What is your name? ")
    if name != "Sam":
        print(name, "is not authorized to exit this loop.")
        continue

    password = input("What is your password? ")
    if password == "huajiao":
        print("你好老师")
        break

    print("Access denied. Try again.")

# This example uses "truthy" and "falsey" values.
# An empty string is falsey. All other strings are truthy.
# This will loop until the user types an answer.
answer = ""
while not answer:
    answer = input("What is your favorite color? ")


# for loops

# Here are two loops that do the same thing.
# I prefer the "for loop" because I don't need to type 'x += 1'.
# (If I forget that line, then the while loop will be infinite!)
x = 1
while x < 4:
    print("This while loop ran", x, "times.")
    x += 1

for x in range(1, 4):
    print("This for loop ran", x, "times.")



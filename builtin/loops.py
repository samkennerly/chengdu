"""
Review of loops from Chapter 3.
"""

# while loops

# I copypasted this example from page 50. I added one line.
spam = 0
while spam < 5:
    print("Hello, world!")
    spam = spam + 1
    print("This loop ran", spam, "times.")

# A dangerous "infinite" loop. It will continue to loop until
# the user enters my name or this Python script crashes.
name = ""
while name != "Sam":
    name = input("What is your name? ")

# A while loop with a 'break' statement.
while True:
    answer = input("What is your favorite language? ")
    if answer != "Python":
        print("I don't like", answer, ". Try again.")
    else:
        print("Python is my favorite language too!")
        break

# A while loop with 'break' and 'continue' statements.
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

# Example of using "truthy" and "falsey" values.
# An empty string is falsey. Any other string is truthy.
# This will loop until the user types an answer.
# Any answer is acceptable.
answer = ""
while not answer:
    answer = input("What is your favorite color? ")

"""
Review of loops from Chapter 3.
"""


# while loops

# Loop example copypasted from page 50.
# In this example, the name 'spam' means nothing.
# It just counts how many times the loop has run.
spam = 0
while spam < 5:
    print('Hello, world!')
    spam = spam + 1


# Another silly loop: print many times the loop has run.
x = 1
while x <= 3:
    print("This loop ran", x, "times")
    x += 1

# A while loop copied from page 52.
# This is an "infinite loop" unless the user types 'your name'.
# (It's not really infinite. It stops when the program crashes.)
name = ''
while name != 'your name':
    print('Please type your name.')
    name = input('>')

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

    # Check the user's name.
    name = input("What is your name? ")
    if name != 'Sam':
        print(name, "is not authorized to exit this loop.")
        continue

    # Check the user's password.
    password = input("What is your password? ")
    if password == 'huajiao':
        print("你好老师")
        break

    print("Access denied. Try again.")

# Example of using "truthy" and "falsey" values.
# An empty string is falsey. Any other string is truthy.
# This will loop until the user types an answer.
# Any answer is acceptable.
answer = ''
while not answer:
    answer = input("What is your favorite color? ")




# Review of Python basics from Chapter 1.


# Say hello

print("Hello, world!")


# Do some arithmetic: 十四是不是四十？

print("10 + 4 is", 10 + 4)
print("10 * 4 is", 10 * 4)


# The ** operator does exponents.

print("10 ** 4 is", 10**4)


# The + operator concatenates strings.

print("'Alice' + 'Bob' is", "Alice" + "Bob")
print("'你' + '好' + '成' + '都' =", "你" + "好" + "成" + "都")


# The * operator replicates a string.

print("5 * 'Alice' is", 5 * "Alice")


# Try using * with a float and a string.
# If it raises an Exception, then print the error message.

try:
    3.14159 * "Alice"
except Exception as err:
    print("Error:", err)


# Create some variables with silly names.

spam = 40
print("spam is", spam)
eggs = 2
print("eggs is", eggs)


# Do some arithmetic with variables.

print("spam + eggs is", spam + eggs)
print("spam + 2 * eggs is", spam + 2 * eggs)


# Mutate a variable, then mutate it again.

spam = spam + 2
print("spam is now ", spam)
spam = spam + 2
print("spam is now ", spam)


# x += y is a shorter way to say x = x + y

spam += 2
print("spam is now", spam)


# Overwite a variable, then overwrite it again.

spam = "Hello"
print("spam is now", spam)
spam = "你好"
print("spam is now", spam)


# These variable names are not allowed.
# If you un-comment these lines, this script will crash.
# 88888888 = "lucky"
# 8eights = "lucky"
# eight8's = "lucky"
# return = "lucky"


# Compare some things of different types.

print("42 == '42'", 42 == "42")
print("42 == 42.0", 42 == 42.0)
print("42.0 == 0042.000", 42.0 == 0042.000)


# Practice using the built-in type() function.

print("42 is a", type(42))
print("42.0 is a ", type(42.0))
print("'42' is a ", type("42"))
print("'四十二' is a ", type("四十二"))


# Practice using the built-in round() function.

pi = 3.1415926535897932384626433
print("round(pi) is", round(pi))
print("round(pi, 3) is", round(pi, 3))
print("type(pi) is", type(pi))
print("type(round(pi)) is", type(round(pi)))
print("type(round(pi, 3)) is", type(round(pi, 3)))


# Practice using the built-in abs() function.

print("abs(25) is", abs(25))
print("abs(-25) is", abs(-25))
print("abs(round(pi, 3)) is", abs(round(pi, 3)))


# I copypasted this code from page 13 of our textbook.
# It's open-source, so I can do that! It's legal.

print("Hello, world!")
print("What is your name?")  # Ask for their name.
my_name = input(">")
print("It is good to meet you, " + my_name)
print("The length of your name is:")
print(len(my_name))
print("What is your age?")  # Ask for their age.
my_age = input(">")
print("You will be " + str(int(my_age) + 1) + " in a year.")

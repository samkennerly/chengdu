# Review of functions from Chapter 4


# I copypasted this function from page 73, then changed it.
# This function does not accept any inputs.


def hello():
    # Prints three greetings
    print("早上好")
    print("下午好")
    print("晚上好")


hello()


# I copypasted this function from page 75, then changed it.
# This function requires one arg (argument): name.


def say_hello_to(name):
    # Prints three greetings to the name provided
    print("早上好 " + name)
    print("下午好 " + name)
    print("晚上好 " + name)


say_hello_to("Ada Lovelace")
say_hello_to("Charles Babbage")


# This function requires two args and returns an output.


def mean(x, y):
    # Mean value of two numbers.
    return (x + y) / 2


print("The mean of -1 and 1 is", mean(-1, 1))
print("The mean of 0 and 100 is", mean(0, 100))
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

z = mean(0, 100)
print("mean(0, 100) returned", z)

s = say_hello_to("Sam")
print("say_hello_to('Sam') returned", s)


# None is a special object with its own type.
# It's an example of a 'null marker'.

print("type(None) is", type(None))


# Some functions accept 'named parameters' as input.
# I call these 'keyword arguments' or 'kwargs'.
# Kwargs are often used for optional inputs.
# In this example, 'name' is a kwarg with default value None.


def say_goodbye(name=None):
    if name is None:
        print("再见")
    else:
        print("再见" + name)


say_goodbye(name="Ada Lovelace")
say_goodbye(name="Charles Babbage")
say_goodbye()


# Many builtin functions accept kwargs. For example, print()
# accepts a kwarg called 'sep'. It means 'separator'.
# If you print many things, Python will insert a separator between
# those things. By default, 'sep' is a space. We can change it:

print("Ada", "Charles", "Guido")
print("Ada", "Charles", "Guido", sep=" & ")

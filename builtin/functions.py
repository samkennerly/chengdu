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


print("The mean of 0 and 100 is", mean(0, 100))
print("The mean of -1 and 1 is", mean(-1, 1))


# I did not tell Python what type x and y should be.
# Python doesn't check argument types. Floats also work:

print("The mean of 0 and 0.1 is", mean(0, 0.1))
print("The mean of 1.5 and 2.5 is", mean(1.5, 2.5))


# If we input the wrong types, Python will still try to call the
# mean() function. It will raise an error and crash.
# print("The mean of '一' and '三' is", mean("一", "三"))

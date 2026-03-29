"""
Review of Python basics.
If you forgot everything over spring break,
this might help to refresh your memory.
"""

print("Hello, world!")

# Do some mathematics
print("10 + 4 =", 10 + 4)
print("10 * 4 =", 10 * 4)
print("10 ** 4 =", 10**4)

# Concatenate strings
print("'Alice' + 'Bob' =", "Alice" + "Bob")

# Replicate a string
print("5 * 'Alice' =", 5 * "Alice")

# Try an illegal operation
try:
    3.14159 * "Alice"
except Exception as err:
    print(err)

# Create some variables with silly names
spam = 40
print("spam =", spam)
eggs = 2
print("eggs =", eggs)

# Do some mathematics with variables
print("spam + eggs =", spam + eggs)
print("spam + 2 * eggs =", spam + 2 * eggs)

# Mutate spam
spam = spam + 2
print("spam = ", spam)
spam = spam + 2
print("spam = ", spam)
spam += 2
print("spam = ", spam)

# Overwite spam
spam = "Hello"
print("spam =", spam)
spam = "你好"
print("spam =", spam)

# These are illegal variable names:
# 88888888 = "lucky"
# 8eights = "lucky"
# eight8's = "lucky"
# return = "lucky"

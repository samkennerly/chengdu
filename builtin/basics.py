"""
Review of Python basics.
If you forgot everything over spring break,
this might help to refresh your memory.
"""

print("Hello, world!")

# Do some mathematics
print("10 + 4 is", 10 + 4)
print("10 * 4 is", 10 * 4)
print("10 ** 4 is", 10 ** 4)

# Concatenate strings
print("'Alice' + 'Bob' is", 'Alice' + 'Bob')

# Replicate a string
print("5 * 'Alice' is", 5 * 'Alice')

# Try something which is not allowed
try:
    3.14159 * "Alice"
except Exception as err:
    print(err)



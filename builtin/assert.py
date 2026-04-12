"""
'assert' statements are often used for automated tests.
The usual pattern is: assert {condition}, {error message}
"""

# Create a variable we can test
spam = 42

# If the condition is True, then assert does nothing.
assert spam == 42, f"{spam} does not equal 42"

# If the condition is False, then this script will crash.
# Python will raise an AssertionError with our error message.
assert spam is None, f"{spam} is not None"

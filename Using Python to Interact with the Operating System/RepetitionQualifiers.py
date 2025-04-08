import re
print(re.search(r"Py.*n", "Pygmalion"))
# searching for Py followed by any number of characters and then n
print(re.search(r"Py.*n", "Python Programming"))
# searching for Py followed by any number of characters and then n
print(re.search(r"Py[a-z]*n", "Python Programming"))
# searching for Py followed by any number of lower case letters and then n
print(re.search(r"Py[a-z]*n", "Pyn"))
# searching for Py followed by any number of lower case letters and then n

# import re
print(re.search(r"o+l+", "goldfish"))
# searching for o followed by one or more l's
print(re.search(r"o+l+", "woolly"))
# searching for o followed by one or more l's
print(re.search(r"o+l+", "boil"))
# searching for o followed by one or more l's

# A greedy regex is a way of writing regular expressions (patterns for matching text) that tries to match as much text as possible, rather than the smallest possible match.
# A "lazy" regex is like a non-greedy regex. Instead of trying to match as much text as possible (like a greedy regex), it tries to match the smallest amount of text possib
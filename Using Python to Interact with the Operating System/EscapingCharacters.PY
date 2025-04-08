import re
print(re.search(r".com", "welcome"))
# searching for ".com" in "welcome" will return None because ".com" is not present in "welcome"
print(re.search(r"\.com", "welcome"))
# searching for ".com" in "welcome" will return None because ".com" is not present in "welcome"
print(re.search(r"\.com", "mydomain.com"))
# searching for ".com" in "mydomain.com" will return a match object because ".com" is present in "mydomain.com"

# import re
print(re.search(r"\w*", "This is an example"))
# searching for "\w*" in "This is an example" will return a match object because "\w*" matches any word character (alphanumeric or underscore) zero or more times
print(re.search(r"\w*", "And_this_is_another"))
# searching for "\w*" in "And_this_is_another" will return a match object because "\w*" matches any word character (alphanumeric or underscore) zero or more times


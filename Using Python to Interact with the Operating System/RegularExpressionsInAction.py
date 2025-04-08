import re
print(re.search(r"A.*a", "Argentina"))
# searching for "A.*a" in "Argentina" will return a match object because "A.*a" matches "Argentina"
print(re.search(r"A.*a", "Azerbaijan"))
# searching for "A.*a" in "Azerbaijan" will return a match object because "A.*a" matches "Azerbaijan"
print(re.search(r"^A.*a$", "Australia"))
# searching for "^A.*a$" in "Australia" will return a match object because "^A.*a$" matches "Australia"

# import re
# declaring a pattern to match a valid variable name in Python\
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
# searching for "^[a-zA-Z_][a-zA-Z0-9_]*$" in "_this_is_a_valid_variable_name" will return a match object because "_this_is_a_valid_variable_name" is a valid variable name
print(re.search(pattern, "this isn't a valid variable"))
# searching for "^[a-zA-Z_][a-zA-Z0-9_]*$" in "this isn't a valid variable" will return None because "this isn't a valid variable" is not a valid variable name
print(re.search(pattern, "my_variable1"))
# searching for  "^[a-zA-Z_][a-zA-Z0-9_]*$" in "my_variable1" will return a match object because "my_variable1" is a valid variable name
print(re.search(pattern, "2my_variable1"))
# searching for "^[a-zA-Z_][a-zA-Z0-9_]*$" in "2my_variable1" will return None because "2my_variable1" is not a valid variable name
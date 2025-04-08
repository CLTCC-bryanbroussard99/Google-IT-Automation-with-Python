import re
print(re.search(r"[Pp]ython", "Python"))
# searching for upper or lower case p

# import re
print(re.search(r"[a-z]way", "The end of the highway"))
# searching for any lower case letter
print(re.search(r"[a-z]way", "What a way to go"))
# returns None because way is preceded by a space
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
# searching for a letter or number after cloud
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))
# searching for a letter or number after cloud

# import re
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
# searching for any character that is not a letter
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
# searching for any character that is not a letter or space

print(re.search(r"cat|dog", "I like cats."))
# searching for cat or dog
print(re.search(r"cat|dog", "I love dogs!"))
# searching for cat or dog
print(re.search(r"cat|dog", "I like both dogs and cats."))
# searching for cat or dog
print(re.findall(r"cat|dog", "I like both dogs and cats."))
# searching for cat or dog and returning all matches
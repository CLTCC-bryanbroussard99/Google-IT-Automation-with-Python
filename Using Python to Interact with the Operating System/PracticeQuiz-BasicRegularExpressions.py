import re
def check_web_address(text):
  pattern = r"^[a-zA-Z0-9._+-]+(\.[a-zA-Z]+)$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

# import re
def check_time(text):
  pattern = r"[1-9][0-2]?:[0-5][0-9] ?(AM|PM|am|pm)"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False

#import re
def contains_acronym(text):
  pattern = r"\([A-Z1-9][a-zA-Z1-9]*\)" 
  result = re.search(pattern, text)
  return result != None
# # \(
# \( is the opening parenthesis character (.
# The backslash \ is used to escape the parenthesis because parentheses 
# are special characters in regex. This makes the regex treat ( as a 
# literal parenthesis, not a special symbol.

# [A-Z1-9]
# This is a character class, meaning it will match one character from the 
# list of allowed characters inside the square brackets [].
# 
# A-Z means any uppercase letter from A to Z.
# 1-9 means any digit from 1 to 9 (not including 0).
# So, [A-Z1-9] matches one uppercase letter (A-Z) or one digit (1-9).

# [a-zA-Z1-9]*
# This is another character class that matches:
# # a-z (any lowercase letter from a to z),
# # A-Z (any uppercase letter from A to Z),
# # 1-9 (any digit from 1 to 9).
# The * means zero or more occurrences of the characters in the class.
# So, this part matches any sequence of letters (either lowercase or 
# uppercase) or digits (1-9), and it can be empty too.

# \)
# \) is the closing parenthesis character ).
# Just like with \(, the backslash escapes the parenthesis to make it a
# literal character instead of a special regex symbol.

# Putting it all together:
# \([A-Z1-9][a-zA-Z1-9]*\) matches:
#   An opening parenthesis (.
#   One uppercase letter (A-Z) or one digit (1-9).
#   Zero or more (but possibly none) characters that are letters 
#       (A-Z or a-z) or digits (1-9).
#   A closing parenthesis ).

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

#import re
def check_zip_code (text):
 result = re.search(r"[ ]\d{5}|[ ]\d{5}-\d{4}", text)
 return result != None

# [ ] :         This part of the pattern matches a space character. It ensures that
#               the zip code is preceded by a space.
# \d{5}:        This part of the pattern matches exactly 5 digits at the 
#               beginning of the string (^ is the start of the string).
# (-\d{4})?:    This part optionally matches the hyphen (-) followed by 4
#               digits. The ? after the parentheses means this part is optional.
# $:            This ensures that the pattern matches up to the end of the 
#               string (no extra characters after the zip code).


print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # True
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False
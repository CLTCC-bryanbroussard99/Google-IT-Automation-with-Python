import re
def long_words(text):
  # \b matches word boundaries, \w matches any word character (alphanumeric + underscore), {7,} means 7 or more occurrences
  pattern = r'\b\w{7,}\b'
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []



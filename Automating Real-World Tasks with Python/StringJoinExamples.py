string1 = "Greetings, Earthlings"

print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”
print(string1[-10:]) # Prints “Earthlings” again
print(string1[55:]) # Prints “”
print(string1[0::2]) # Prints “Getns atlns”
print(string1[::-1]) # Prints “sgnilhtraE ,sgniteerG”
#
phonenum = '2025551212'

area_code = phonenum[:3] # The first 3 digits are the area code:
prefix =  phonenum[3:6] # Digits 4-4 are the prefix:
final_four =  phonenum[7:10] # Final Four digits are the particular home or device.:
print (area_code + '.' + prefix + '.' + final_four)

def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line

print ( format_phone('2025551212') )
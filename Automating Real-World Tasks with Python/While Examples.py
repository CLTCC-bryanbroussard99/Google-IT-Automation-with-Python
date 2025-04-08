num = 0

while num < 5:
    num = num + 1
    print('num = ', num)

print('Break------------------------------------------------')

num = 0

while num < 5:
    num += 1   # num += 1 is same as num = num + 1
    print('num = ', num)
    if num == 3: # condition before exiting a loop
        break

print('Continue------------------------------------------------')

num = 0

while num < 5:
	num += 1   # num += 1 is same as num = num + 1
	if num == 3: # condition before exiting a loop
		continue
	print('num = ', num)

print('Else------------------------------------------------')

num = 0

while num < 3:
	num += 1   # num += 1 is same as num = num + 1
	print('num = ', num)
else:
    print('else block executed')

print('Sum Average------------------------------------------------')

num=0
count=0
sum=0

while num>=0:
    num = int(input('enter any number .. -1 to exit: '))
    if num >= 0:
        count = count + 1 # this counts number of inputs
        sum = sum + num # this adds input number cumulatively.
avg = sum/count
print('Total numbers: ', count, ', Average: ', avg)

def square(x):
    return x*x

numbers=[1, 2, 3, 4, 5]
sqrs_of_numbers=map(square, numbers)
next(sqrs_of_numbers)
next(sqrs_of_numbers)
next(sqrs_of_numbers)
next(sqrs_of_numbers)
next(sqrs_of_numbers)
#In the above example, the map() function applies to each element in the numbers list. This will return an object of the map class, which is an iterator, and so, we can use the next() function to traverse the list.

#Map with Lambda Expression
#The map() function passes each element in the list to the built-in functions, a lambda function, or a user-defined function, and returns the mapped object. The following map() is used with the lambda function.

#Example: map() with lambda functionCopy
sqrs_of_numbers = map(lambda x: x*x, [1, 2, 3, 4])
    next(sqrs_of_numbers)
    next(sqrs_of_numbers)
    next(sqrs_of_numbers)
    next(sqrs_of_numbers)
    next(sqrs_of_numbers)
#Map with Built-in Function
#In the following example, a built-in function pow() is given to map two list objects, one for each base and index parameter. The result is a list containing the power of each number in bases raised to the corresponding number in the index.

#Example: map() with built-in functionCopy
bases=[10, 20, 30, 40, 50]
index=[1, 2, 3, 4, 5]
powers=list(map(pow, bases, index))
powers [10, 400, 27000, 2560000, 312500000]




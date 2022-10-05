# Author: Jonathan Doherty
# GitHub username: Dohertyj11
# Date: 9/21/2022
# Description: Asks the user for five numbers and then prints out the average of those numbers.


print('Please enter five numbers you wish to be averaged.')

number1 = input('1st number: ')
int1 = float(number1)
number2 = input('2nd number: ')
int2 = float(number2)
number3 = input('3rd number: ')
int3 = float(number3)
number4 = input('4th number: ')
int4 = float(number4)
number5 = input('5th number: ')
int5 = float(number5)

total = int1 + int2 + int3 + int4 +int5
average = total / 5

print('The average is', average)

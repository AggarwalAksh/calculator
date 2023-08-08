#getting the numbers
print('Welcome to the calculator')
print('Enter a number')
num1 = float(input())
print('Enter another number')
num2 = float(input())

#choosing the method of operation
print('Pick a number')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplacation')
print('4.Division')
method = int(input())

#doing the calculation
if method == 1:
  result = num1 + num2
  print('The answer is',result)
elif method == 2:
  result = num1 - num2
  print('The answer is',result)
elif method == 3:
  result = num1 * num2
  print('The answer is',result)
elif method == 4:
  result = num1 / num2
  print('The answer is',result)
else:
  print('invalid method')
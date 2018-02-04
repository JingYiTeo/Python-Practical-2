from fractions import gcd

digit1 = int(input("Enter first integer: "))
digit2 = int(input("Enter second integer: "))

print("The Greatest Common Divisor of {} and {} is {}.".format(digit1, digit2, gcd(digit1,digit2)))

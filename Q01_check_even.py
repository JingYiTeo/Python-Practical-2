# Key in values:
Number = int(input("Enter a number: "))


#remainder after dividing by 2
Remainder = Number % 2

#remainder must be 0
if Remainder > 0:
    print("{} is odd".format(Number))
else:
    print("{} is even".format(Number))

#Enter year
Year = int(input("Enter year: "))

#Divide
A = Year % 4
B = Year % 100
C = Year % 400

#if else
if A == 0 and B > 0 or C == 0:
    print("Leap")
else:
    print("Non-Leap")

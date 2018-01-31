#Values for sides:

A = float(input("Enter side 1: "))
B = float(input("Enter side 2: "))
C = float(input("Enter side 3: "))

#if else
if A+B > C and A+C > B and B+C > A:
    P = A + B + C
    print("Perimeter = {:.2f}".format(P))
else:
    print("Invalid triangle!")

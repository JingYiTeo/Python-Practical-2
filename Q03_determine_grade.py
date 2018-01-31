#Enter score

Score = int(input("Enter score: "))

if Score >= 70 and Score <= 100:
    print("A")
elif Score >= 60 and Score <= 69:
    print("B")
elif Score >=55 and Score <= 59:
    print("C")
elif Score >= 50 and Score <=54:
    print("D")
elif Score >= 45 and Score <=49:
    print("E")
elif Score >= 35 and Score <= 44:
    print("S")
elif Score >= 0 and Score <= 35:
    print("U")
else:
    print("Invalid! Score must be within 0 - 100.")
    
    

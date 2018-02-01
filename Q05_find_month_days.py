#user details:

Month = int(input("Enter Month(in numbers): "))
Year = int(input("Enter Year: "))

#Leap
A = Year % 4
B = Year % 100
C = Year % 400

#Arrays:

M = [ 'Nothing', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
LDays = [ '0', '31', '29', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
NLDays = [ '0', '31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31'] 

#if else
if A == 0 and B > 0 or C == 0:
    AnsMonths = M[Month]
    Days = LDays[Month]
    print("{} {} has {} days.".format(AnsMonths,Year,Days))
else:
    Months = M[Month]
    NDays = NLDays[Month]
    print("{} {} has {} days.".format(Months,Year,NDays))

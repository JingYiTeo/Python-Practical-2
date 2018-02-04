print("Miles", "Kilometres", "Kilometres", "Miles")
    

for i in range(0,10):
    i = i + 1
    KM = i * 1.609
    f = i*5 + 20
    KM2 = f/1.609
    print("\n{}".format(i) + "\t{:.3f}".format(KM) + "\t{}".format(f) + "\t{:.3f}".format(KM2))

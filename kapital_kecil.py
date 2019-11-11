def ganti(x):
    y=''
    for i in range(len(x)):
        if x[i].islower()==True:
            y+=x[i].upper()
        else:
            y+=x[i].lower()
    return y
print(ganti('AbcdEFgHi'))
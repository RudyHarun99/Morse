from functools import reduce

class hitung:
    def rata(self,x):
        mean=reduce(lambda a,b:a+b,x)/len(x)
        return mean
    def tengah(self,x):
        x.sort()
        if len(x)%2!=0:
            itengah=[int(len(x)/2)]
        else:
            itengah=[int(len(x)/2-1),int(len(x)/2)]
        atengah=list(map(lambda a:x[a],itengah))
        median=reduce(lambda x,y:x+y,atengah)/len(atengah)
        return median
    def modus(self,x):
        modus = max(set(x), key=x.count)
        a = x.count(modus)
        b = []
        for i in x:
            if a - 1 < x.count(i):
                b.append(i)
        c = b[::a]
        modus1 = 'Modus data adalah '
        modus2 = []
        if len(c) == 1:
            modus1 += str(c[0])
        else:
            for i in c:
                modus2.append(str(i))
            modus1 += ' & '.join(modus2)
    
        print(modus)
        return

stat=hitung()
print(stat.modus([10,1,3,2,5,4,6,8,7,9]))

#mean
# from functools import reduce
# angka=[1,2,3,4,5,6,7,8,9,5]
# print(len(angka))
# z=reduce(lambda x,y:x+y,angka)

# mean=(reduce(lambda x,y:x+y,angka))/(len(angka))
# print(mean)

#median
# a=sorted(angka)
# print(a)

#mode
# angka=[1,2,3,4,5,6,7,8,9,5,9]
# hasil=[]
# for x in angka:
#     y=angka.count(x)
#     hasil.append(y)
# print(hasil)
# z=max(hasil)
# print(z)
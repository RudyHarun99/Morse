'''
#map without lambda (using function)
def times2(num) :
    return num * 2
listNum = [ 1, 2, 3, 4, 5]
listNum = list(map(times2, listNum))
print(listNum)

#map with lambda
listNum = [ 1, 2, 3, 4, 5]
listNum = list(map(lambda num: num * 2, listNum))
print(listNum)

#filter without lambda
def genap(num) :
    return num % 2 == 0
listNum = [ 1, 2, 3, 4, 5]
listNum = list(filter(genap, listNum))
print(listNum)

#filter with lambda
listNum = [ 1, 2, 3, 4, 5]
listNum = list(filter(lambda num: num % 2 == 0, listNum))
print(listNum)

#searching
numList = [1,2,3]
input = 'x'
check1 = input in numList 
check2 = 'x' in ['x','y','z']
check3 = 'ka' in 'kurakas'
print(check1)
print(check2)
print(check3)
'''

# x=['Merdeka','Hello','Hellos','Sohib','Kari ayam']
# cari=input('Search : ')
# hasil=[]
# for a in range(len(x)):
#     y=x[a].lower()
#     cek=cari in y
#     a+=1
#     if cek==True:
#         hasil.append(y)
# print(hasil) 

'''
x=lambda a:a    #pake lambda
def y(a):       #pake function, kira2 fungsinya sama dengan lambda
    return a    #lambda function dipake klo perlu function tp ga mau bikin function
print(x(2))
print(y(2))
print(type(x))  #type x adlh lambda function

x=lambda a,b,c:a+b+c
def y(a,b,c):
    return a+b+c
print(x(2,3,4))
print(y(2,3,4))

def myfunction(x):
    return lambda a:a**x

pangkat2=myfunction(2)
pangkat3=myfunction(3)
pangkat5=myfunction(5)

print(pangkat2(12))
print(pangkat3(4))
print(pangkat5(2))

x=lambda a:True if a%2==0 else False    #fungsi if else di dalam lambda function
print(x(4))

def y(a):   #fungsi if else pake function def
    if a%2==0:
        return True
    else:
        return False
print(y(4))

x=lambda a:'Angka Genap' if a%2==0 else 'Angka Ganjil'  #fungsi if else di dalam lambda function
print(x(4))

x=lambda a:print(a)
x('Hello')  #memanggil fungsi lambda dgn nilai 'Hello', hasilnya string 'Hello'
print(x('Hello'))   #menghasilkan 'None'

#map phyton pake function
def y(a):
    return len(a)
a=['Andilala','Budiman','Caca']
x=map(y,a)
print(x)
print(list(x))
x=map(y,'Purwadhika')
print(list(x))

a=['Cokelat','Melon','Nangka']
b=['Apel','Jeruk','Nanas']
def combi(a,b):
    return a+' '+b
x=map(combi,a,b)
print(x)
print(list(x))

x=[2,4,6,8,10]
def pangkat(a):
    return a**2
y=map(pangkat,x)
print(y)
print(list(y))

#map pake lambda
z=map(lambda a:a**2,x)
print(list(z))

b=[]
for i in x:
    b.append(i**2)
print(b)
'''

#filter python pake function
x=range(11)
print(list(x))

def kuranglima(x):
    if x<5:
        return False
    else:
        return True

#filter pake lambda
y=filter(kuranglima,x)
print(list(y))

z=filter(lambda a:True if a>=5 else False,x)
print(list(z))

x=pow(2,2)
y=pow(3,3)
print(x)
print(y)

z=list(map(pow,[2,3],[2,3]))
print(z)

x=[1,2,3,4,5,99]
y=[1,2,6,7,8,99]
z=list(filter(lambda a:a in x,y))
print(z)

#reduce, menggunakan semua elemen utk operasi, pake cara function
angka=[1,2,3,4]
hasil=1
for i in angka:
    hasil*=i
print(hasil)

#reduce tanpa cara function
from functools import reduce
z=reduce(lambda x,y: x*y,angka)
print(z)

import math
print(math.pi)

from math import pi
print(pi)

kata=['Ini','Ibu','Budi']
print(''.join(kata))

from functools import reduce
z=reduce(lambda x,y: x+y, kata)
print(z)

angka=[1,2,3,4]
z=list(map(lambda x:x*2,filter(lambda x:x>3,angka)))
print(z)
z=list(filter(lambda x:x>3,map(lambda x:x*2,angka)))
print(z)

from functools import reduce
nomor=list(range(1,101))
z=reduce(lambda x,y:x+y,list(map(lambda x:x*2,filter(lambda x:x%2==0,nomor))))
print(z)
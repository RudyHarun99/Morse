# def hello():
#    print('Hello World!')

# hello();hello();hello()

# def kuadrat():
#    print(2**2)
# kuadrat()

# def kuadrat(x):
#    print(x**2)
# kuadrat(2)
# kuadrat(3)

# def pangkat(angka1,angka2):
#    print(angka1**angka2)
# pangkat(2,3)
# pangkat(2,10)

# def pangkat(angka1,angka2):
#    print(angka1**angka2)

# pangkat(float(input('Ketik angka 1 :')),float(input('Ketik angka 2 :')))

# def gage(x):
#    if x%2==0:
#       print(x,'tergolong GENAP')
#    else:
#       print(x,'tergolong GANJIL')
# gage(2.9)
# gage(99.28678)
# gage(int(input('Ketik angka : ')))

# def fungsi():
#    x=int(input('1. Masukkan angka 1 : '))
#    op=input('2. Masukkan operator aritmatika (+-/*) : ')
#    y=int(input('3. Masukkan angka 2 : '))
#    if op =='+':
#       print(x,op,y,'=',x+y)
#    elif op =='-':
#       print(x,op,y,'=',x-y)
#    elif op =='/':
#       print(x,op,y,'=',x/y)
#    elif op =='*':
#       print(x,op,y,'=',x*y)
#    else:
#       print('Operator salah')

# fungsi()

# def vocal(text):
#    vokal=['a','i','u','e']
#    text=text.lower()
#    text=text.replace(vokal[0],'o')
#    text=text.replace(vokal[1],'o')
#    text=text.replace(vokal[2],'o')
#    text=text.replace(vokal[3],'o')
#    print(text)

# vocal('kuda')
# vocal('air mata')
# vocal('lintang')
# vocal('rudi harun')
# vocal('Selamat datang!')
# vocal('Aiueo')

#return function
def luaspersegi(sisi):
   luas=sisi*sisi
   return luas

sisiA=6
luaspersegiA=luaspersegi(sisiA)
print(luaspersegiA)

def gage(angka):
   if angka%2==0:
      return 'GENAP'
   else:
      return 'GANJIL'
print(gage(30))
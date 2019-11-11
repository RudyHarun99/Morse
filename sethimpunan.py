x=[1,2,3,1,2,3]
y=(1,2,3,1,2,3)

z={1,2,3}       #set/himpunan tidak ada index
print(type(z))

z={1,2,3,1,2,3} #tidak boleh ada duplikat elemen
print(z)

print(set(x))   #mengubah menjadi set
print(set(y))   #mengubah menjadi set

print(list(x))  #kembali menjadi list
print(tuple(y)) #kembali menjadi tuple

z.add('a')      #menambah nilai dalam set, hanya 1 nilai
print(z)

z.add(('c','d','e'))    #set mutable, tapi isinya harus immutable, ga bisa diisi list
print(z)

z.update('andi')        #menambah nilai dalam set, tapi akan dipecah menjadi 'a','n','d','i'
print(z)

z.update([6,7,8])       #menambah list, elemennya dipecah
print(z)

z.update({'z','budi'})  #menambah set dengan nilai 'z' dan 'budi'
print(z)

print('budi' in z)      #cek nilai 'budi', ada di set z atau tidak, nilainya boolean
z.remove('budi')        #menghapus nilai 'budi'
print(z)

z.discard('deni')       #tdk error walaupun nilainya ga ada, klo remove akan error
print(z)

z.pop()                 #menghapus nilai depan di set
print(z)

z.clear()               #menghapus semua elemen
print(z)

# del z                   #menghapus set z
# print(z)

a={'a','b','c','d','e'}
b={'b','c','f','g','h'}
print(a.intersection(b))    #mencari irisan a terhadap b
print(a&b)                  
print(b.intersection(a))    #mencari irisan b terhadap a
print(b&a)                  

print(a.union(b))    #gabungan a terhadap b
print(a|b)           
print(b.union(a))    #gabungan b terhadap a
print(b|a)           

print(a.difference(b))  #a dikurang b
print(a-b)              
print(b.difference(a))  #b dikurang a
print(b-a)

print(a.symmetric_difference(b))  #a di luar irisan b
print(a^b)               
print(b.symmetric_difference(a))  #b di luar irisan a
print(b^a)

p={1,2,4,7,9,19}
q={7,9,5,6,12,16,17,19}
r={3,8,6,19}
print(p.intersection(q))
print(p&q)
print(p.intersection(q.intersection(r)))
print(p&q&r)

p={-4,-3,-2,-1,0,1,2,3,4,}
q={-7,-6,-5,-4,-3,-2,-1,0,1}
r={-1,0,1,2,3,4,5,6,7}
s={-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9}
print(p|q)
print(p|r)
print(q|r)

x=set([1,2,3])
y=frozenset([1,2,3])    #set yang immutable, ga bisa diubah
print(x)
print(y)
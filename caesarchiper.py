alfabet=[
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
]

kata=input('Masukkan kata : ')
listkata=list(kata)
hasil=''
for a in range(len(listkata)):
    huruf=listkata.index(listkata[a])
    hasil+=alfabet[huruf+2]
    a+=1
print(hasil)

def prima(x):
    a=False
    if x>1:
        if x==2:
            a=True
        for i in range(2,x):
            if x%i==0:
                a=False
                break
            else:
                a=True
    else:
        a=False
    return a
print(prima(12))
print(prima(13))
print(prima(2))

angka=list(range(2,101))
z=list(filter(prima,angka))
print(z)

nums=range(2,101)
for i in range(2,8):
    nums=list(filter(lambda x:x==i or x%i,nums))
    print(f'ini i : {i}')
print(nums)

'''
# Program python untuk menentukan bilangan prima atau tidak
# Meminta input bilangan dari user
num = int(input("Masukkan bilangan: "))
# bilangan prima harus lebih besar dari 1
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "bukan bilangan prima")
            print(i, "kali", num//i, "=", num)
            break
    else:
        print(num,"adalah bilangan prima")
# bila bilangan kurang atau sama dengan satu
else:
    print(num, "bukan bilangan prima")
'''    
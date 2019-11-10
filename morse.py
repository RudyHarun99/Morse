sandi={
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..'
}

kata=input('Ketik kata : ')
listpisah=list(kata.upper())
listhuruf=list(sandi.keys())
listmorse=list(sandi.values())
hasil=''
if listpisah[0] in listhuruf:
    for a in range(len(listpisah)):
        huruf=listhuruf.index(listpisah[a])
        morse=listmorse[huruf]
        hasil+=morse+'/'
        a+=1
    print(hasil)
else:
    listpisah=kata.split('/')
    for a in range(len(listpisah)):
        morse=listmorse.index(listpisah[a])
        huruf=listhuruf[morse]
        hasil+=huruf
        a+=1
    print(hasil.capitalize())
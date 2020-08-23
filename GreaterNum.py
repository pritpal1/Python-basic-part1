a = int(input('enter 1st value'))
b = int(input('enter 2nd value'))
c = int(input('enter 3rd value'))
if a>b & a>c:
    print(a,': is Greater')
elif b>a & b>c:
    print(b,': is Greater')
else:
    print(c,': is Greater')
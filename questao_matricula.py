m1 = int(input('digite a matricula 1_'))
m2 = int(input('digite a matricula 2_'))
m3 = int(input('digite a matricula 3_'))
if m1>m2>m3 or m1>m3>m2:
    print('o maior é',m1)
    if m2>m3:
        print('o menor é',m3)
    else:
        print('o menor é',m2)
elif m2>m1>m3 or m2>m3>m1:
    print('o maior é',m2)
    if m1>m3:
        print('o menor é',m3)
    else:
        print('o menor é',m1)
elif m3>m1>m2 or m3>m2>m1:
    print('o maior é',m3)
    if m1>m2:
        print('o menor é',m2)
    else:
        print('o menor é',m1)
print('Bem vindo ao conversor de Temperaturas!!!')
print('Escolha a operação desejada')
print('A para obter em C°')
print('B para obter em F°')
op = str(input('digite a operação_'))

if op == 'A' or 'a' or 'fahrenheit' or 'Fahrenheit':
    tempf = float(input('Insira a Temperatura em F°_'))
    c = tempf*5/9-32*5/9
    print('A Temperatura é',c,'° celsius')
elif op == 'B' or 'b' or 'celsius' or 'Celsius':
    tempc = float(input('Insira a Temperatura em C°_'))
    f = tempc*9/5+32
    print('A Temperatura é',f,'° fahrenheit')
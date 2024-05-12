print('selecione a operação desejada')
print('A: conversão para REAL')
print('B: conversão para DOLAR')
op = str(input('insira a operacao_'))
cot = float(input('Insira a cotação atual do dolar_'))
if op == 'b':
    rel = float(input('Insira o valor em REAL_'))
    dol = rel/cot
    print('o valor é',dol,'dolares')
elif op == 'a':
    dol = float(input('Insira o valor em DOLAR_'))
    rel = dol*cot
    print('o valor é',rel,'reais')
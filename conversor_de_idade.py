#primeira parte, conversor de idade
print('Insira sua idade no formato A/M/D')
ano = int(input('anos_'))
mes = int(input('meses_'))
dia = int(input('dias_'))
print('sua idade é',ano,'anos',mes,'meses','e',dia,'dias')
anod = ano*365
mesd = mes*30
soma = anod+mesd+dia
print('sua idade em dias é',soma,'dias')
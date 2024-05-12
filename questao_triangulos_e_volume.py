import sys
ld1 = float(input('Insira a medida do lado_'))
ld2 = float(input('Insira a medida do lado_'))
ld3 = float(input('Insira a medida do lado_'))
c1 = ld1-ld2-ld3
c2 = ld2-ld1-ld3
c3 = ld3-ld1-ld2
#determina se o triangulo existe
if ld1 <= 0 or ld2 <= 0 or ld3 <= 0:
    print('Erro, medida inválida')
else:
    if c1 > 0 or c2 > 0 or c3 > 0:
        print('O triângulo não existe')
        sys.exit(1)
    else:
        p = ld1+ld2+ld3
        area = float((p*(p-ld1)*(p-ld2)*(p-ld3))**0.5)
        print('a area do triangulo é',area)
#determina o tipo do triângulo
if ld1==ld2==ld3:
    print('o triângulo é equilátero')
elif ld1==ld2 or ld1==ld3 or ld2==ld3:
    print('o triangulo é isóceles')
else:
    print('o triangulo é escaleno')
#calcular o volume de uma caixa
comp = float(input('Digite o Comprimento_'))
alt = float(input('Digite a Altura_'))
prof = float(input('Digite a Profundidade_'))
vol = comp*alt*prof
print('o volume é',vol)
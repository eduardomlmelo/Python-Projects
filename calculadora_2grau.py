print('Vamos resolver uma equacao do tipo: ax^2 + bx +c')
a = float(input('Insira o coeficiente_'))
b = float(input('Insira o coeficiente_'))
c = float(input('Insira o coeficiente_'))
d = b**2 - 4*a*c
if d >= 0:
    x1 = (-b+(d)**0.5)/2*a
    x2 = (-b-(d)**0.5)/2*a
    if x1 == x2:
        print('a equacao possui apenas uma raiz igual a',x1)
    else:
        print('a equacao possui duas raizes reais iguais a',x1,'e',x2)
elif d < 0:
    print('a equacao nao possui raizes reais')

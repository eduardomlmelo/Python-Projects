num1 = float(input('Digite o 1° número_'))
num2 = float(input('Digite o 2° número_'))
if num1 > num2:
    if num2 == 0:
        print('divisão inválida')
    else:
        num3 = num1/num2
        if num3 % 1 == 0:
            print(num1,'e',num2,'são multiplos')
        else:
            print(num1,'e',num2,'não são multiplos')
elif num2 > num1:
    num3 = num2/num1
    if num1 == 0:
        print('divisão inválida')
    else:
        if num3 % 1 == 0:
            print(num1,'e',num2,'são multiplos')
        else:
            print(num1,'e',num2,'não são multiplos')
elif num1 == num2 == 0:
    print('indeterminação encontrada')
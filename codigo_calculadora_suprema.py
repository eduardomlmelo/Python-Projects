def calculadora():
    print("Bem vindo(a) à calculadora, insira, a seguir, os números e operação")
    num1 = int(input('digite o 1 numero_'))
    op = str(input('digite a operacao_'))
    num2 = int(input('digite o 2 numero_'))
    if op == '+' or op == 'soma':
        soma=num1+num2
        print(num1,"+",num2,"=",soma)
    elif op == '-' or op == 'subtracao':
        sub = num1-num2
        print(num1,"-",num2,"=",sub)
    elif op == '*' or op == 'multiplicacao':
        mul = num1*num2
        print(num1,"*",num2,"=",mul)
    elif op == '/' or op == 'divisao':
        if num2 == '0':
            print('erro')
        else:
            div = float(num1/num2)
            print(num1,"/",num2,"=",div)
def somatorioInt():
    print("Bem vindo ao somatório de inteiros")
    i = int(input("Digite a quantidade de termos desejada: "))
    soma = 0
    j=1
    while j<=i:
        soma += j
        j+=1
    print(f"A soma dos termos (1,{i}) é: {soma}")
def somador():
    num = 1
    soma = 0
    print("Digite os números desejados(0 para interromper)")
    while num != 0:
        num = int(input("_"))
        soma+=num
    print("O resultado é: ",soma)

def main():
    print("Bem vindo ao programa CALCULADORA SUPREMA")
    print("1: para calculadora padrão")
    print("2: para somatório de inteiros")
    print("3: para somatório de inteiros dados")
    op = str(input("Digite a operação desejada "))
    if op == "1" or op == "calculadora":
        calculadora()
    elif op == "2" or op == "somatorio":
        somatorioInt()
    elif op == "3" or op == "somador":
        somador()
main()
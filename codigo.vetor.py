vetor = []
i = 1
n = int(input('Tamanho da lista_'))

def main():     
    vector = []
    i = 1
    n = int(input('Tamanho da lista_'))
    while i <= n:
        value = int(input(''))
        vector.append(value)
        i = i + 1

while i <= n:
    valor = int(input(''))
    vetor.append(valor)
    i = i + 1

print('a lista está correta?',vetor)

res = str(input('_'))

if res == 'sim' or 's':
    menor = min(vetor)
    print('O menor número é:',menor)
elif res == 'não' or 'nao' or 'n':
    vetor = []
    print('Ok, resetei a lista, vamos de novo...')
    if __name__ == '__main__':
        main()
        print("A lista está correta agora?",vetor)
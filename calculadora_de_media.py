#primeira parte, média do aluno
nome = str(input('digite o nome do aluno(a)_'))
nota1 = int(input('digite a 1° nota_'))
nota2 = int(input('digite a 2° nota_'))
nota3 = int(input('digite a 3° nota_'))
media = (2*nota1+3*nota2+5*nota3)/10
print('A média de',nome,'é',media)
#segunda parte, situação do aluno
if media >= 7:
    print(nome,'está APROVADO')
else:
    print(nome,'está REPROVADO e fudido(a)')
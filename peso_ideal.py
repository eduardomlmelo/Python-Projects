print('bem vindo ao calculador de peso ideal')
gen = str(input('Por favor, digite seu gênero_'))
if gen == 'M' or 'Homem' or 'homem':
    h = float(input('Agora, digite sua altura_'))
    peso = float(72.7*h-58)
    print('O peso ideal para sua altura é',peso)
elif gen == 'F' or 'Mulher' or 'Mulher':
    h = float(input('Agora, digite sua altura_'))
    peso = float(61.2*h-44.7)
    print('O peso ideal para sua altura é',peso)
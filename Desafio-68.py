import random
contador = 0
result = plural = ' '
print('=' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    print('=' * 30)
    jogador = int(input('Digite um número: '))
    pc = random.randint(0, 10)
    soma = jogador + pc
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('=' * 30)
    print(f'Você jogou {jogador} e o Computador {pc}. O total deu {soma} então ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P':
        if soma % 2 == 0:
            print('=' * 30)
            print('VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            contador += 1
        else:
            print('=' * 30)
            print('VOCÊ PERDEU!')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('=' * 30)
            print('VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            contador += 1
        else:
            print('=' * 30)
            print('VOCÊ PERDEU!')
            break
if contador <= 1:
    plural = 'vez'
elif contador > 1:
    plural = 'vezes'
print('=' * 30)
print(f'GAME OVER! Você venceu {contador} {plural}.')

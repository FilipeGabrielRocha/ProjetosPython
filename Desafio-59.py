import time
pergunta = ''
numero1 = int(input('Primeiro valor: ').strip())
numero2 = int(input('Segundo valor: ').strip())
while pergunta != 5:
    pergunta = int(input('''[ 1 ] SOMAR.
[ 2 ] MULTIPLICAR.
[ 3 ] MAIOR.
[ 4 ] NOVOS NÚMEROS.
[ 5 ] SAIR DO PROGRAMA.
Digite o número para executar a tarefa: ''').strip())
    if pergunta == 1:
        somar = numero1 + numero2
        print(f'\nVocê escolheu : SOMAR.\nA soma entre {numero1} + {numero2} = {somar}.')
        time.sleep(2)
    elif pergunta == 2:
        mult = numero1 * numero2
        print(f'\nVocê escolheu: MULTIPLICAR.\nA multiplicação entre os números {numero1} x {numero2} = {mult}.')
        time.sleep(2)
    elif pergunta == 3:
        if numero1 == numero2:
            print(f'\nOs valores {numero1} e {numero2} são iguais.')
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
            print(f'\nVocê escolheu: MAIOR.\nO maior número entre {numero1} e {numero2} é {maior}.')
        time.sleep(2)
    elif pergunta == 4:
        print('\nDigite os dois novos valor.')
        numero1 = int(input('Primeiro valor: ').strip())
        numero2 = int(input('Segundo valor: ').strip())
        time.sleep(2)
    elif pergunta == 5:
        print('\nPreparando para fechar o programa...')
        time.sleep(2)
        print('Programa fechado!\nFIM')
    else:
        print('Número Inválido. Digite novamente.')
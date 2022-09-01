# biblioteca de tempo
from time import sleep

# variaveis para guargar numeros inteiros
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o proxímo número: '))

# opcao para validação dos valores do menu
opcao = 0

# loop para execucao do programa
while opcao != 7:
    print('''Digite dois número inteiros e escolha uma das opções abaixo:
    [1] Soma 
    [2] Subtração   
    [3] Multiplicação
    [4] Divisão
    [5] Mudar valores
    [6] Maior
    [7] Sair ''')
    opcao = int(input('Escolha uma opção acima: '))

# validando as opcoes sugeridas no menu
    if opcao == 1:
        print('A soma de {} + {} é igual a {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('O valor {} - {} é igual a {}'.format(n1, n2, n1-n2))
    elif opcao == 3:
        print('A multiplicação de {} * {} é {}'.format(n1, n2, n1*n2))
    elif opcao == 4:
        print('O quociente de {} / {} é {}'.format(n1, n2, n1/n2))
    elif opcao == 5:
        print('Digite os novos valores: ')
        n1 = int(input('digite o novo valor: '))  
        n2 = int(input('Digite o proxímo valor: '))
    elif opcao == 6:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif opcao == 7:
        print('Obrigador por chegar até aqui. Volte sempre')
    elif opcao :
        print('opcao invalida!!! Por Favor tente novamente.')
    print('=-=-=-'*20)
    sleep(3)
print('Fim')
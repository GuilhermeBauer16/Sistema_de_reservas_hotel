def titulo(msg, quant=40):
    quantia = quant * 2
    print('=' * quantia)
    print(f'{msg:^{quantia}}')
    print('=' * quantia)


def conversor_numero(msg,type):

    while True:
        opcao = input(msg)
        try:
            num_opcao = type(msg)
            break
        except ValueError:
            print('\033[31mPor favor selecione um número\033[m')


def quartos():
    titulo('imformações sobre os quartos')
    print('''
    [1]Quarto simples
    [2]Quanto para 2 pessoas
    [3]Quarto familia
    [4]Quarto de luxo
    [5]Suite presidencial
    ''')
    print('=' * 80)
    opcao = conversor_numero('Imforme o quarto que deseja saber mais: ',int)

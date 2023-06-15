def titulo(msg, quant=40):
    quantia = quant * 2
    print('=' * quantia)
    print(f'{msg:^{quantia}}')
    print('=' * quantia)


def conversor_numero(msg,tipo = int):

    while True:
        opcao = input(msg)
        try:
            num_opcao = tipo(opcao)
            break
        except ValueError:
            print('\033[31mPor favor selecione um número\033[m')
    return num_opcao

def quartos():
    titulo('imformações sobre os quartos')
    print('''
    [1]Quarto simples
    [2]Quanto duplo
    [3]Quarto familia
    [4]Quarto de luxo
    [5]Suite presidencial
    [6]sair 
    ''')
    print('=' * 80)
    opcao = conversor_numero('Imforme o quarto que deseja saber mais: ',int)
    if opcao == 1: 
        titulo('Quarto simples')
        print("""O quarto simples é uma opção aconchegante e econômica para uma pessoa. 
Ele oferece uma cama confortável, um espaço tranquilo e os itens essenciais 
para uma estadia confortável.""")
        print()
        print('valor R$ 100,00 a diária ')
    
    elif opcao == 2:
        titulo('Quarto duplo')
        print("""O quarto duplo é ideal para casais ou amigos
que desejam compartilhar acomodações. Esse quarto oferece uma 
ou duas camas de casal, garantindo um descanso tranquilo para ambos os hóspedes.
 Além disso, possui comodidades básicas para atender às necessidades de duas pessoas.""")
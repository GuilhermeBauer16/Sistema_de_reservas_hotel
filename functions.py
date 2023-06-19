from time import sleep
def titulo(msg, quant=40):
    quantia = quant * 2
    print('=' * quantia)
    print(f'{msg:^{quantia}}')
    print('=' * quantia)

def conversor_numero(msg,tipo = int):

    while True:
        opcao = input(msg).strip()
        try:
            num_opcao = tipo(opcao)
            break
        except ValueError:
            print('\033[31mPor favor selecione um número\033[m')
    return num_opcao

def quartos():
    opcaos_validas = [1,2,3,4,5,6]
    escolha = ''
    valor = ''
    while True:
        titulo('imformações sobre os quartos')
        print('''
        [1]Quarto simples
        [2]Quanto duplo
        [3]Quarto familia
        [4]Quarto de luxo
        [5]Suite presidencial
        [6]Já me decidi  
        ''')
        print('=' * 80)
        opcao = conversor_numero('Imforme o quarto que deseja saber mais: ',int)
        if opcao in opcaos_validas:
            if opcao == 1: 
                titulo('Quarto simples')
                print("""O quarto simples é uma opção aconchegante e econômica para uma pessoa. 
Ele oferece uma cama confortável, um espaço tranquilo e os itens essenciais 
para uma estadia confortável.""")
                print()
                print('valor R$ 100,00 a diária ')
                print('=' * 80)
                sleep(1)

            elif opcao == 2:
                titulo('Quarto duplo')
                print("""O quarto duplo é ideal para casais ou amigos
que desejam compartilhar acomodações. Esse quarto oferece uma 
ou duas camas de casal, garantindo um descanso tranquilo para ambos os hóspedes.
Além disso, possui comodidades básicas para atender às necessidades de duas pessoas.""")
                print()
                print('valor R$ 200,00 a diária ')
                print('=' * 80)
                sleep(1)

            elif opcao == 3:
                titulo('Quarto Familiar') 
                print("""O quarto familiar é projetado para acomodar famílias ou grupos
maiores. Ele geralmente inclui camas espaçosas o suficiente para 
acomodar adultos e crianças, proporcionando conforto e privacidade para todos. 
Também pode oferecer recursos adicionais, como área de estar ou espaço de recreação 
para a família desfrutar de momentos juntos.""")
                print()
                print('valor R$ 400,00 a diária ')
                print('=' * 80)
                sleep(1)

            elif opcao == 4:
                titulo('Quarto de luxo')
                print('''O quarto de luxo é um ambiente elegante e sofisticado, oferecendo
um alto nível de conforto e comodidades extras. Normalmente, possui uma decoração 
requintada, mobiliário de qualidade, roupas de cama luxuosas e recursos adicionais,
como TV de tela grande, minibar, banheiro espaçoso ou vista panorâmica.
                ''')
                print()
                print('valor R$ 1000,00 a diária ')
                print('=' * 80)
                sleep(1)

            elif opcao == 5:
                titulo('Suíte presidencial')
                print("""A suíte presidencial é a acomodação mais luxuosa e exclusiva 
disponível no hotel. Ela é projetada para proporcionar uma experiência excepcional,
oferecendo um espaço amplo e refinado. Geralmente, possui um quarto separado, 
uma área de estar sofisticada, uma sala de jantar privativa e comodidades exclusivas
, como banheira de hidromassagem, sauna privativa ou terraço com vista panorâmica""")
                print()
                print('valor R$ 5000,00 a diária ')
                print('=' * 80)
                sleep(1)
            

            elif opcao == 6:
                opcaos_validas = [1, 2, 3, 4, 5]
                while True:
                    titulo('Que bom que você se decidiu')
                    quarto = conversor_numero('Informe o quarto de sua escolha: ', int)
                    if quarto in opcaos_validas:
                        if quarto == 1:
                            escolha = 'Quarto simples'
                            valor = 100.00
                        elif quarto == 2:
                            escolha = 'Quarto duplo'
                            valor = 200.00
                        elif quarto == 3:
                            escolha = 'Quarto Familiar'
                            valor = 400.00
                        elif quarto == 4:
                            escolha = 'Quarto de luxo'
                            valor = 1000.00
                        elif quarto == 5:
                            escolha = 'Suíte presidencial'
                            valor = 5000.00
                        break
                    else:
                        print('\033[31mSelecione uma opção válida\033[m')
                break
        else:
            print('\033[31mSelecione uma opção válida\033[m')

    return escolha , valor

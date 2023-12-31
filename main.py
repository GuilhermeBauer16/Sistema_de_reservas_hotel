import pymysql
import functions
from time import sleep
connection = pymysql.connect(

    host='127.0.0.1',
    port= 3306, 
    user='root',
    password='0910',
    database='reservas_hotel'

)
nome_reserva = ''
escolha = ''
quarto = ''
diaria = ''
banco = """CREATE DATABASE IF NOT EXISTS reservas_hotel 
            DEFAULT CHARACTER SET utf8 
            DEFAULT COLLATE utf8_general_ci """

cursor = connection.cursor()
cursor.execute(banco)

def autentica_usuario():
    global nome_reserva
    while True:
        functions.titulo('Usuarios' , 40 )
        nome_reserva = str(input('Imforme seu nome completo para conferir sua reserva[0 para voltar ao menu]: ')).upper().replace(' ','_')
        if nome_reserva == '0':
            break
        cursor.execute(f'SHOW TABLES LIKE "{nome_reserva.replace(' ', '_').upper()}"')
        resultado = cursor.fetchone()
        if resultado:
            cursor.execute(f'SELECT * FROM {nome_reserva}')
            reservas = cursor.fetchall()
            functions.titulo(f'{nome_reserva.replace("_", " ")}')
            for reserva in reservas:
                print(f'Nome: {reserva[1].replace("_", " ")}')
                print(f'Quarto: {reserva[2]}')
                print(f'dias: {reserva[3]}')
                print(f'R$: {reserva[4]}')
            print('=' * 80)
            functions.titulo('Funções Adicionais')
            print('''
[1]Editar reserva
[2]Deletar reserva
[3]Voltar ao menu
''')
            print('=' * 80)
            opção_reserva = functions.conversor_numero('Sua opção: ', int)
            print('=' * 80)
            if opção_reserva == 1:

                novo_quarto, nova_diaria = functions.quartos() 
                novo_dias = functions.conversor_numero('Quantos dias você ira permanecer no quarto: ',int)# 1- quarto 2-valor do quarto
                novo_total = nova_diaria * novo_dias 

                update =  (f"""
                               UPDATE {nome_reserva} SET quarto = %s , dias= %s ,
                               soma = %s WHERE nome = %s  """)
                
                valores_atualizados = (novo_quarto , novo_dias , novo_total , nome_reserva)
                cursor.execute(update,valores_atualizados)
                connection.commit()
                print(f'\033[32m{nome_reserva.replace('_' , ' ')} sua reserva foi alterada com sucesso\033[m ')
                sleep(1.5)
                functions.limpa_terminal()

            elif opção_reserva == 2:

                cursor.execute(f'DROP TABLE {nome_reserva} ')
                print(f'\033[32mreserva no nome de {nome_reserva.replace('_',' ')} deletada\033[m')
                sleep(1.5)
                functions.limpa_terminal()

            elif opção_reserva == 3: 

                print('Voltando para o menu')
                sleep(1.5)
                functions.limpa_terminal()
                break
        

        else: 
            print('\033[31mNão possue usuario cadastrado neste nome\033[m')



while True:
    functions.titulo('Reservas do Hotel')
    print("""
[1]Nova reserva  
[2]Ja possue reserva
[3]sair  """)
    print('=' * 80)
    opção = functions.conversor_numero('Sua opção: ' , int)

    if opção == 1:
        functions.titulo('Nova reserva',40)
        nome_completo = str(input('Imforme seu nome completo: ')).upper().replace(' ','_') 
        quarto, diaria = functions.quartos() 
        dias = functions.conversor_numero('Quantos dias você ira permanecer no quarto: ',int)# 1- quarto 2-valor do quarto
        total = diaria * dias 

        try: 
            usuario = f'''CREATE TABLE IF NOT EXISTS {nome_completo}(
                        id INT NOT NULL AUTO_INCREMENT ,
                        Nome VARCHAR(150) NOT NULL ,
                        quarto VARCHAR(21) ,
                        dias TINYINT, 
                        soma decimal(9,2) ,
                        PRIMARY KEY (id))
                        default charset = utf8'''
            
            cursor.execute(usuario)

            cadastro = f'''
            INSERT INTO {nome_completo}(
            nome , quarto , dias , soma ) 
            VALUES (%s , %s , %s , %s )'''

            valores = (nome_completo, quarto , dias , total )
            cursor.execute(cadastro,valores)
            connection.commit()
            print(f'\033[32mUsuario {nome_completo.replace('_', ' ')} cadrastado com sucesso\033[m')

        except pymysql.Error as erro:
            print('\033[31mJa possue um usuario cadastrado neste nome\033[m')
            print(f'erro {erro}')
        sleep(2)
        functions.limpa_terminal()

    elif opção == 2:
            
            autentica_usuario() 
           
    elif opção == 3:
        print('saindo...')
        sleep(1)
        break

    else:
        print('\033[31mPor favor digite uma opção valida\033[m')

#SQL

cursor.close()
connection.close()



import pymysql
import functions
connection = pymysql.connect(

    host='127.0.0.1',
    port= 3306, 
    user='root',
    password='0910',
    database='reservas_hotel'

)
 
cursor = connection.cursor()
# cursor.execute('DROP TABLE trhyrthrh')

def mostrar():
    cursor.execute('''SELECT table_name FROM information_schema.tables WHERE table_schema = "reservas_hotel"
    ''')
    tabelas  = cursor.fetchall()

    for tabela in tabelas:
        print(tabela[0])


escolha = ''
quarto = ''
diaria = ''
while True:
    functions.titulo('Reservas do Hotel Bauer ')
    print("""
[1]Nova reserva  
[2]Ja possue reserva  """)
    print('=' * 80)
    opção = functions.conversor_numero('Sua opção: ' , int)

    if opção == 1:
        functions.titulo('Nova reserva')
        nome_completo = str(input('Imforme seu nome completo: ')).upper().replace(' ','_') # 1- quarto 2-valor do quarto
        quarto, diaria = functions.quartos() 
        dias = functions.conversor_numero('Quantos dias você ira permanecer no quarto: ',int)
        total = diaria * dias 

        try: 
            usuario = f'''CREATE TABLE IF NOT EXISTS {nome_completo}(
                        Nome VARCHAR(255) ,
                        quarto VARCHAR(255) ,
                        dias TINYINT, 
                        soma FLOAT )'''
            
            cursor.execute(usuario)

            cadastro = f'''
            INSERT INTO {nome_completo}(
            nome , quarto , dias , soma ) 
            VALUES (%s , %s , %s , %s )'''

            valores = (nome_completo, quarto , dias , total )
            cursor.execute(cadastro,valores)
            connection.commit()
            print(f'Usuario {nome_completo.replace('_', ' ')} cadrastado com sucesso')

        except pymysql.Error as erro:
            print(f'erro {erro}')

    elif opção == 2:
        mostrar() 
        while True:
            functions.titulo('Usuarios' , 80 )
            nome_reserva = str(input('Imforme seu nome completo para convefir sua reserva: ')).upper().replace(' ','_')
            cursor.execute(f'SELECT * FROM {nome_reserva}')
            reservas = cursor.fetchall()
            functions.titulo(f'{nome_reserva.replace("_", " ")}')
            for reserva in reservas:
                print(f'Nome: {reserva[0].replace("_", " ")}')
                print(f'Quarto: {reserva[1]}')
                print(f'dias: {reserva[2]}')
                print(f'R$: {reserva[3]}')
            print('=' * 80)
        
    
    break

#SQL

cursor.close()
connection.close()



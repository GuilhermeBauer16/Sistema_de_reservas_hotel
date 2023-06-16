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
# try :
#     create_table_query = '''
#     CREATE TABLE reservas (
#         id INT NOT NULL AUTO_INCREMENT,
#         usuario INT NOT NULL,
#         PRIMARY KEY (id)
#     )
#     '''
#     cursor.execute(create_table_query)
#     print('Tabela "reservas" criada com sucesso.') 


# except pymysql.Error as erro:
#     print(f'erro {erro}')

escolha = ''
quarto = ''
valor = ''
while True:
    functions.titulo('Reservas do Hotel Bauer ')
    print("""
[1]Nova reserva  
[2]Ja possue reserva  """)
    print('=' * 80)
    opção = functions.conversor_numero('Sua opção: ' , int)

    if opção == 1:
        functions.titulo('Nova reserva')
        nome_completo = str(input('Imforme seu nome completo: ')).upper()
        quarto, valor = functions.quartos() 
        print(quarto)
        print(valor)


    elif opção == 2:
        while True:
            functions.titulo('Usuarios', )
        
    
    break

#SQL
cursor.close()
connection.close()



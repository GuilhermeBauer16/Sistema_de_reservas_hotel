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
try :
    create_table_query = '''
    CREATE TABLE reservas (
        id INT NOT NULL AUTO_INCREMENT,
        usuario INT NOT NULL,
        PRIMARY KEY (id)
    )
    '''
    cursor.execute(create_table_query)
    print('Tabela "reservas" criada com sucesso.') 


except pymysql.Error as erro:
    print(f'erro {erro}')

functions.titulo('Reservas')
print("""
[1]Imformações quartos 
[2]clientes """)
print('=' * 80)
opção = functions.conversor_numero('Sua opção: ' , int)

while True:

    if opção == 1:

        if functions.quartos() == 'sair':
            break
        else:
            functions.quartos()
            
    elif opção == 2:
        while True:
            functions.titulo('Usuarios', )
            print("""
[1]Novo usuario
[2]Usuarios 
[3]Voltar ao menu
        """
              )

#SQL
cursor.close()
connection.close()



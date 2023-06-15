import pymysql
import functions
connection = pymysql.connect(

    host='localhost',
    port= 3306, 
    user='root',
    password='0910',
    database='reservas_hotel'

)
cursor = connection.cursor()

# cursor.execute(""" CREATE TABLE reservas (
#     id INT NOT NULL AUTO_IMCREMENT PRIMARY KEY 
#     usuario "
# )
# """)
functions.titulo('Reservas')
print("""
[1]Imformações quartos 
[2]clientes """)

opção = functions.conversor_numero('Sua opção: ' , int)

while True:

    if opção == 1:
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



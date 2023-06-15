import pymysql
import functions
connection = pymysql.connect(

    host='localhost',
    user='root',
    password='0910',
    database='reservas_Hotel'

)
cursor = connection.cursor()

functions.titulo('Reservas')
print("""
[1]Imformações quartos 
[2]clientes """)

#SQL
cursor.close()
connection.close()



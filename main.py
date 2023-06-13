import sqlite3
from pathlib import Path



connection = sqlite3.connect('reservasHotel.db')
cursor = connection.cursor()


pessoa = str(input("Por favor imforme seu nome: "))

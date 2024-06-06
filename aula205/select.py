import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE) # Conectando a banco de dados
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME} LIMIT 2')

for row in cursor.fetchall():
    _id, name, weight = row # Desempacotando a tupla
    print(_id, name, weight)


cursor.close()
connection.close()
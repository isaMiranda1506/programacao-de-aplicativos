import sqlite3

def cadastrar_hoteis():
    conexao = sqlite3.conecct('hotelaria.db')
    cursor = cursor.execute()

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hoteis(
                id INTEGER PRIMARY KEY,
                nome_hotel TEXT NOT NULL,
                cidade TEXT NOT NULL 
            )
        ''')
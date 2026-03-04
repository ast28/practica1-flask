import sqlite3

# Fitxer on estarà la base de dades local
DB_NAME = "grup.db"

# Funció per connectar amb fitxer base de dades
def get_connection():
	return sqlite3.connect(DB_NAME)

# Inicialitza base de dades, creant taula 'grup' si no existeix
def init_db():
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS grup (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT NOT NULL)""")
	conn.commit() 	# Guarda els canvis
	conn.close() 	# Tanca connexió

# Es connecta a la bd, guarda els noms i es desconnecta
def guardar_grup(noms):
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute("DELETE FROM grup")
	for nom in noms:
		cursor.execute("INSERT INTO grup (nom) VALUES (?)", (nom,))
	conn.commit()
	conn.close()

# Es connecta a la bd, selecciona i retorna els noms guardats i es desconnecta
def carregar_grup():
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT nom FROM grup")
	resultats = cursor.fetchall()
	conn.close()
	return [fila[0] for fila in resultats]

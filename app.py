from flask import Flask, render_template, request
from database import init_db, guardar_grup, carregar_grup

# Crea la instància de la aplicació Flask
app = Flask(__name__)

# Inicialitza la base de dades
init_db()
# Defineix la ruta principal, accepta GET i POST
@app.route("/", methods=["GET", "POST"])
def index():
	# Si l'usuari ha enviat dades al formulari
	if request.method == "POST":
		# Guardarem els noms a la llista de la base de dades
		noms_text = request.form.get("noms")
		if noms_text:
			grup = [nom.strip() for nom in noms_text.split(",")]
			guardar_grup(grup)
	# Recuperar la llista actualitzada i la mostrarà bonic index.html passant-li la llista 
	grup = carregar_grup()
	return render_template("index.html", grup=grup)
	
# Punt d'entrada per executar el servidor
if __name__ == "__main__":
	# Executa la aplicació escoltant al port indicat i sense mode debug
	app.run(host="0.0.0.0", port=8000, debug=False)

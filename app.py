from flask import Flask, render_template, request
from database import init_db, guardar_grup, carregar_grup
app = Flask(__name__)
init_db()
@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		noms_text = request.form.get("noms")
		if noms_text:
			grup = [nom.strip() for nom in noms_text.split(",")]
			guardar_grup(grup)
	grup = carregar_grup()
	return render_template("index.html", grup=grup)
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug=False)

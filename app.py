from flask import Flask, render_template

app = Flask(__name__)
# route -> milhapremiada.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
   return render_template("index.html")
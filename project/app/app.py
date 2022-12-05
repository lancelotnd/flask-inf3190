import os
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)
@app.route("/")
def salut():
    return render_template("form.html")


@app.route("/diresalut", methods=['GET', 'POST'])
def submit(): 

    nom = request.form["nom"]
    prenom = request.form["prenom"]
    age= request.form["age"]
    error = None

    if not nom or not nom.strip():
        error = "Il manque le nom"
    if not prenom or not prenom.strip():
        error = "Il manque le prenom"
    if not age or not age.strip():
        error = "Il manque l'age"

    if error:
        return render_template("form.html", nom=nom, prenom=prenom, age=age, error=error)


    return redirect(url_for('foo'))
    
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8050)
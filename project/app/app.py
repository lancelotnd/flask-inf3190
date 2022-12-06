from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("lab11.html")

@app.route("/submit", methods=["POST"])
def submit():
    prenom = request.form["prenom"]
    nom = request.form["nom"]
    age = request.form["age"]

    error = ""

    if not prenom:
        error += "Le prénom doit être non nul /"
    if not nom:
        error += "Le nom doit être non nul /"
    if not age:
        error += "L'âge doit être non nul /"

    if error != "":
        return render_template("lab11.html", error=error, nom=nom, prenom=prenom, age=age)

    with open("db.txt", "a") as fichier:
        fichier.write(f"{nom}, {prenom}, {age}\n")
    return redirect(url_for("results"))


@app.route("/results")
def results():
    results = []
    lines = open("db.txt", "r").readlines()
    for line in lines:
        result = line.split(",") # [nom, prenom, age]
        results.append(result)
        print(result)
    print(results)
    return render_template("results.html", results=results, len=len(results))


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8050)
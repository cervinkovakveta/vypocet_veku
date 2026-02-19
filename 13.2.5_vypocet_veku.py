
# naimportujeme z modulu flask třídu Flask, funkce render_template() a objekt request (objekt požadavku)
from flask import Flask, render_template, request

# vytvoří instanci třídy Flask
app = Flask(__name__)

# přidá další webovou stránku "vypocet_veku"
@app.route("/vek", methods=["GET", "POST"])
def vypocet_veku():
    vek = None

    # po vyplnění formuláře vypočítá a zobrazí výsledky
    if request.method =="POST":
        try:
            rok_narozeni = int(request.form["rok_narozeni"])
            
            # vypočítá vek
            vek= 2026 - rok_narozeni
        except ValueError:
            pass
    return render_template("vek.html", vek_uzivatele_html=vek)

# zkontroluje jestli byl program spuštěný na přímo
if __name__ == "__main__":
    # spustí server Flask - ladící režim zapnutý, na portu 5000
    app.run(debug=True, port=5000)
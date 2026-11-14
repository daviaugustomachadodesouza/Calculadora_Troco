from duracao import paraCentavos, centavo
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/" , methods=["GET", "POST"])
def inicio():
    resultadoTroco = None
    erro = None
    valorDigitado = ""

    if request.method == "POST":
        valorDigitado = request.form.get["valor", ""]
        try:
            centavos = paraCentavos(valorDigitado)
            resultadoTroco = centavo(centavos)
        except ValueError as e:
            erro = str(e)
    return render_template(
        "index.html",
        pecas = resultadoTroco,
        erro = erro,
        valorOriginal = valorDigitado,
    )

if __name__ == "__main__":
    app.run(debug=True)
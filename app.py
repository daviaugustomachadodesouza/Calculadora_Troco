from duracao import paraCentavos, centavo
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    resultadoTroco = None
    erro = None
    valorDigitado = ""

    if request.method == "POST":
        # Correção aqui: uso de parênteses em vez de colchetes
        valorDigitado = request.form.get("valor", "")
        try:
            centavos = paraCentavos(valorDigitado)
            resultadoTroco = centavo(centavos)
        except ValueError as e:
            erro = str(e)
            
    return render_template(
        "index.html",
        pecas=resultadoTroco,
        erro=erro,
        valorOriginal=valorDigitado,
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

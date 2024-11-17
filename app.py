from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ejercicio1")
def ejercicio1():
    return render_template("ejercicio1.html")

@app.route("/ejercicio2")
def ejercicio2():
    return render_template("ejercicio2.html")

@app.route("/procesar1", methods=["POST"])
def procesar1():
    nota1 = int(request.form.get("nota1"))
    nota2 = int(request.form.get("nota2"))
    nota3 = int(request.form.get("nota3"))
    asistencia = int(request.form.get("asistencia"))

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 40 and asistencia >= 75:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    return f"""
    <h1>Formulario de Notas</h1>
    <p>Nota 1: {nota1}</p>
    <p>Nota 2: {nota2}</p>
    <p>Nota 3: {nota3}</p>
    <p>Asistencia: {asistencia}%</p>
    <p>Promedio: {promedio:.1f}</p>
    <h2>{estado}</h2>
    <a href="/">Volver al Menú Principal</a>
    """

@app.route("/procesar2", methods=["POST"])
def procesar2():
    nombre1 = request.form.get("nombre1")
    nombre2 = request.form.get("nombre2")
    nombre3 = request.form.get("nombre3")

    nombres = [nombre1, nombre2, nombre3]
    nombre_mas_largo = max(nombres, key=len)
    longitud = len(nombre_mas_largo)

    return f"""
    <h1>Resultados</h1>
    <p>El nombre con mayor cantidad de caracteres es: <strong>{nombre_mas_largo}</strong></p>
    <p>El nombre tiene: <strong>{longitud}</strong> caracteres</p>
    <a href="/">Volver al Menú Principal</a>
    """
if __name__ == "__main__":
    app.run(debug=True)



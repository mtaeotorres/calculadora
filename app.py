from flask import Flask, render_template, request

app = Flask(__name__)

# Lógica de las operaciones matemáticas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División entre cero"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener los valores ingresados por el usuario
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operacion = request.form['operacion']

        # Realizar la operación seleccionada
        if operacion == "sumar":
            resultado = suma(num1, num2)
        elif operacion == "restar":
            resultado = resta(num1, num2)
        elif operacion == "multiplicar":
            resultado = multiplicacion(num1, num2)
        elif operacion == "dividir":
            resultado = division(num1, num2)
        else:
            resultado = "Operación no válida"
        
        return render_template('index.html', resultado=resultado)

    return render_template('index.html', resultado=None)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

print("Iniciando la aplicación Flask...")

app = Flask(__name__)

@app.route('/')
def home():
    print("Renderizando la página de inicio...")
    return render_template('index.html')

if __name__ == '__main__':
    print("Ejecutando la aplicación Flask...")
    app.run(debug=True, port=5001)

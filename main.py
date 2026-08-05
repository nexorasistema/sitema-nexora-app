from flask import Flask, render_template

# Crear la aplicación
aplicacion = Flask(__name__)

# Ruta de prueba principal
@aplicacion.route('/')
def inicio():
    return "✅ ¡Sistema Nexora funcionando correctamente!"

# Ejecutar la app
if __name__ == "__main__":
    aplicacion.run(host="0.0.0.0", port=5000)

from flask import Flask, render_template, request, jsonify

# Crear la aplicación
app = Flask(_name_)

# Ruta de prueba principal
2am@app.route('/')
def inicio():
    return "✅ Sistema Nexora funcionando correctamente!"

# Ejecutar la app en Render
if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)

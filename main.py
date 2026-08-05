from flask import Flask, render_template, request, jsonify, send_file
import os
import json
from datetime import datetime

# Inicializar la aplicación
aplicacion = Flask(_name_)

# ---------------------- PÁGINA PRINCIPAL ----------------------
@aplicacion.route('/')
def inicio():
    return render_template('index.html')

# ---------------------- PÁGINAS DE PROYECTOS ----------------------
@aplicacion.route('/proyecto/river-building')
def river_building():
    return render_template('river_building.html')

@aplicacion.route('/proyecto/ambienza')
def ambienza():
    return render_template('ambienza.html')

@aplicacion.route('/proyecto/los-prados')
def los_prados():
    return render_template('los_prados.html')

# ---------------------- COTIZADOR Y CRM ----------------------
@aplicacion.route('/cotizar', methods=['GET', 'POST'])
def cotizar():
    if request.method == 'POST':
        datos = request.form.to_dict()
        # Aquí se procesan los datos para generar la cotización
        return jsonify({"mensaje": "Cotización generada correctamente", "datos": datos})
    return render_template('cotizar.html')

@aplicacion.route('/crm')
def crm():
    return render_template('crm.html')

# ---------------------- EJECUCIÓN EN RENDER ----------------------
if _name_ == "_main_":
    aplicacion.run(host="0.0.0.0", port=5000, debug=False)

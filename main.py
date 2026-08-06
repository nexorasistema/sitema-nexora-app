from flask import Flask, render_template, send_from_directory

app = Flask(_name_, 
            template_folder='nexora',
            static_folder='nexora')

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/<path:ruta>')
def rutas(ruta):
    return send_from_directory('nexora', ruta)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=10000)

from flask import Flask

aplicacion = Flask(_name_)

@aplicacion.route('/')
def inicio():
    return "✅ Sistema Nexora funcionando correctamente!"

if _name_ == "_main_":
    aplicacion.run(host="0.0.0.0", port=5000)
  

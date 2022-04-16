
# Created by RamPanic

from flask import ( abort,
                    Blueprint, 
                    request,
                    jsonify )

from utils.bna import divisas, billetes


bna = Blueprint("bna", __name__) 


# ================================================================== #
#                                                                    #
#                           Rutas para BNA                           #
#                                                                    #
# ================================================================== #

@bna.route("/api/divisas")
def obtener_divisas():

    lista_divisas = divisas()

    return jsonify(lista_divisas)

@bna.route("/api/divisas/<int:identificador>")
def obtener_divisa(identificador):
    
    lista_divisas = divisas()

    if identificador > len(lista_divisas) - 1:
        return { "error": "No existe el id solicitado" }

    return lista_divisas[identificador]

@bna.route("/api/billetes")
def obtener_billetes():

    lista_billetes = billetes()

    return jsonify(lista_billetes)

@bna.route("/api/billetes/<int:identificador>")
def obtener_billete(identificador):
    
    lista_billetes = billetes()

    if identificador > len(lista_billetes):
        return { "error": "No existe el id solicitado" }

    return lista_billetes[identificador]

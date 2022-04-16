
# Created by RamPanic

import requests

from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from collections import OrderedDict

def divisas():
    
    url_divisas = "https://bna.com.ar/Cotizador/MonedasHistorico"

    response = requests.get(url_divisas).text

    soup = BeautifulSoup(response, "html.parser")

    tabla = soup.find_all("tbody")

    filas = tabla[0].find_all("tr")

    divisas = list()

    for ident, fila in enumerate(filas[0:]):
    
        columnas = fila.find_all("td")
    
        divisa = OrderedDict()    
        divisa["id"] = ident
        divisa["moneda"] = columnas[0].text
        divisa["compra"] = columnas[1].text
        divisa["venta"] = columnas[2].text

        divisas.append(divisa)

    return divisas

def billetes():

    dias = 0

    encontrado = False

    while not encontrado:

        fecha = datetime.today() - timedelta(days=dias)

        dia = fecha.day
        mes = fecha.month
        anio = fecha.year

        url_billetes = f"https://bna.com.ar/Cotizador/HistoricoPrincipales?id=billetes&fecha={dia}%2F{mes}%2F{anio}&filtroEuro=1&filtroDolar=1"

        response = requests.get(url_billetes).text

        if not "No hay cotizaciones pendientes para esa fecha" in response:

            encontrado = True

        dias += 1

    soup = BeautifulSoup(response, "html.parser")

    tablas = soup.find_all("tbody") 

    billetes = list()

    for ident, tabla in enumerate(tablas):
        
        columnas = tabla.find_all("td")

        billete = OrderedDict()
        billete["id"] = ident
        billete["moneda"] = columnas[0].text
        billete["compra"] = columnas[1].text
        billete["venta"] = columnas[2].text
        billete["fecha"] = columnas[3].text

        billetes.append(billete)

    return billetes

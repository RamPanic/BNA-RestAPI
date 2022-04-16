<p align="center"><img height="100" src="https://i.imgur.com/a0IKdkq.png" alt="BNA-API">
<br>
<br>
<img src="https://img.shields.io/badge/Creado%20por-RamPanic-green">
<img src="https://img.shields.io/badge/Hecho en%20-Python3-red">
    <a href="https://github.com/RamPanic?tab=repositories"><img src="https://img.shields.io/badge/Ver%20m%C3%A1s-repositorios-yellow"></a>
</p>

Un RESTful API para los billetes principales y las cotizaciones del BNA - https://bna-restapi.herokuapp.com/

Nota: ésta RestAPI no es oficial.

## Setup <img src="https://img.shields.io/badge/Python-3.10.2-green">

Clonamos el repositorio

```
git clone https://github.com/RamPanic/BNA-RestAPI.git
```

Instalamos las dependencias

```
pip3 install -r requirements.txt
```

En caso que aparezcan errores para otra versión de Python, basta con instalar solo las siguientes:

```
BeautifulSoup4
requests
flask
```

Luego editamos el archivo config.py a nuestro gusto.

## Iniciar servidor

```
python runserver.py
```

## Recursos

* /api/divisas
* /api/divisas/\<id>
* /api/billetes
* /api/billetes/\<id>

## Palabras finales

Esto fue desarrollado para un trabajo en el cual una empresa solicitaba los valores de los billetes y cotizaciones del BNA. Pero lo malo de esto, es que ésta no tiene una RestAPI para obtener dichos valores, entonces decidí crear una a partir de hacer WebScraping en la misma. Si bien no tiene muchos recursos a consumir, es una buena oportunidad para que empresas la usen sin necesidad de realizar labores extra de Scraping en sus programas.

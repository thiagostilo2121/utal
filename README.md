
# PyUTAL For Python

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/thiagostilo2121/utal)
[![PyPi](https://img.shields.io/badge/pypi-%23ececec.svg?style=for-the-badge&logo=pypi&logoColor=1f73b7)]()
[![LICENSE](https://img.shields.io/badge/LICENSE-MIT-%23ececec.svg?style=for-the-badge&logo=LICENSE&logoColor=1f73b7)](LICENSE)

PyUTAL (Unnoficial TikTok Automatization Library) es una librería de Python para desarrollar chatbots o automatizaciones en chat/bandeja de mensajes de TikTok (no chat de TikTok Live) usando Selenium.

## Instalación

Para instalar PyUTAL, utilizaremos el gestor de paquetes `pip`. Sin embargo, antes, es recomendable crear un entorno virtual de la siguiente manera.

 - Instalamos `virtualenv` si es que no lo tenemos.
   - `pip install virtualenv`
 - Creamos el entorno virtual.
   -  `python3 -m venv venv`
 - Lo inicializamos.
   - En windows
   - `venv/Scripts/activate.ps1`
   - En Linux/MacOs
   - `source venv/bin/activate`

Una vez instalado, creado e inicializado el entorno virtual, instalaremos `utal` de la siguiente forma.
`pip install utal`

## Comienzo rápido
Aquí se presenta una guía para un proyecto simple en `utal`.

python

import utal as ut
from selenium import webdriver

def startup_selenium():
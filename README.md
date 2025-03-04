# PyUTAL For Python

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/thiagostilo2121/utal)
[![PyPi](https://img.shields.io/badge/pypi-%23ececec.svg?style=for-the-badge&logo=pypi&logoColor=1f73b7)]()
[![LICENSE](https://img.shields.io/badge/LICENSE-MIT-%23ececec.svg?style=for-the-badge&logo=LICENSE&logoColor=1f73b7)](LICENSE)

PyUTAL (*Unofficial TikTok Automation Library*) es una librería de Python diseñada para desarrollar chatbots o automatizaciones en la bandeja de mensajes de TikTok (no en TikTok Live) utilizando Selenium.

## Instalación

Para instalar PyUTAL, se recomienda primero crear un entorno virtual para aislar las dependencias del proyecto. Sigue estos pasos:

1. Instalar `virtualenv` si aún no lo tienes:
   ```sh
   pip install virtualenv
   ```
2. Crear un entorno virtual:
   ```sh
   python3 -m venv venv
   ```
3. Activar el entorno virtual:
   - **Windows:**
     ```sh
     venv\Scripts\activate
     ```
   - **Linux/macOS:**
     ```sh
     source venv/bin/activate
     ```
4. Instalar `utal` dentro del entorno virtual:
   ```sh
   pip install utal
   ```

## Comienzo rápido

A continuación, se presenta una guía para iniciar un proyecto simple con `utal`.

1. Inicializa el `webdriver` con Selenium **sin** el modo `headless` la primera vez para poder iniciar sesión en la cuenta del bot.
2. Luego, usa el siguiente código:

```python
import os
import utal as ut
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def startup_selenium():
    USERDATADIR = os.path.abspath("path/to/user/data/directory")
    DRIVERPATH = "path/to/webdriver"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless")  # Ejecutar sin headless la primera vez
    options.add_argument(rf"user-data-dir={USERDATADIR}")
    
    driver = webdriver.Chrome(service=Service(DRIVERPATH), options=options)
    return driver  # Importante retornar el driver

def main(driver):
    driver.get("https://tiktok.com/messages")
    
    while True:  # Importante usar bucles
        message = ut.Client.listen(driver=driver)  # Devuelve todos los mensajes
        print(message)

if __name__ == "__main__":
    driver = startup_selenium()
    main(driver)
```

## Notas importantes
- **El modo `headless` debe desactivarse la primera vez** para poder iniciar sesión manualmente en TikTok y guardar los datos de sesión.
- **Es necesario utilizar un bucle** para que el bot pueda escuchar continuamente los mensajes entrantes.

## Licencia
Este proyecto está licenciado bajo la **MIT License**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

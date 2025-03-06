from setuptools import setup, find_packages

setup(
    name="utal",  # Nombre de tu librería
    version="0.2.0",  # Versión de la librería
    packages=find_packages(),  # Encuentra los paquetes de tu librería
    install_requires=[  # Aquí especificas las dependencias
        "selenium",  # Esto le dice a pip que instale Selenium automáticamente
    ],
    # Otras configuraciones opcionales
    author="Thiago Valentín Stilo Limarino",
    author_email="stilothiagovalentin@gmail.com",
    description="Unnoficial TikTok library for chatbot making. Use at your own risk.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/thiagostilo2121/utal",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)

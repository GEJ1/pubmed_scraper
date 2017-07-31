# Pubmed_Scraper ![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo")


## Trabajo práctico final del [Curso de Python de la UTN fra]( http://www.lslutnfra.com/curso-python "Curso de Python de la UTN fra").  Docente: lucas.bais@gmail.com

### Descripción: Scraper de abstracts del motor de búsqueda de artículos científicos PubMed [PubMed]( https://www.ncbi.nlm.nih.gov/pubmed/ "PubMed"). Incluye un proceso básico de data minning y data visualization usando [nltk](http://www.nltk.org/ "nltk") y [regular expressions(RE)](https://docs.python.org/3.4/library/re.html).

Modo de instalación:

1)  Ejecutar desde una terminal estando en el directorio adecuado `pip install -r requirements.txt`

2) Instalar los datos que requiere nltk para funcionar: 
Se debe ejectutar desde una terminal estando en el directorio adecuado `python nltk_download_data.py` , esperar a que se abra una ventana emergente,  seleccionar all package y darle download.
Más información entrando a [Installing NLTK Data](http://www.nltk.org/data.html).

3) Ejecutar desde una terminal estando en el directorio adecuado "python scraper.py descargar 'cantidad de papers' 'partes en la que se dividirá la descarga' " donde ambos
son números enteros. Ejemplo `python scraper.py descargar 100 10 ` descargará 100 abstracts en 10 partes, cada archivo se llamará 'abstract_#.txt', con # = numero de abstract. Se recomienda no generar partes de más de 100 abstracts.

4) Ejecutar desde una terminal estando en el directorio adecuado `python scraper.py limpiar.py` . 
Este script pre procesa el texto (borra usando la librería re, caracteres que se repiten o son menos informativos (es modificable)) y genera un archivo "Todos_los_abstracts.txt"

5) Ejecutar desde una terminal estando en el directorio adecuado `python nltk_tokenization.py` y seguir las instrucciones para obtener gráficos de dispersión o de frecuencia de palabras.
La propia biblioteca nltk implementa [matplotlib](https://matplotlib.org/) para hacer los gráficos.

6) Ejecutar desde una terminal estando en el directorio adecuado `python scraper.py borrar` para borrar todos los abstracts y poder comenzar de nuevo desde cero.

 

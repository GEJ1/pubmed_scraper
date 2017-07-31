#coding=utf-8

from subprocess_library import  procesar
from Scraper_pubmed_library import Scraper_pubmed
import sys


# El orden de parametros es 1) descargar o borrar. En caso de seleccionar descargar: 2) Cantidad a descargar 3) cantidad de partes en las cuales dividir la descarga

if __name__== '__main__':
		
	
	if 	sys.argv[1] == 'descargar':
		procesar(int(sys.argv[2]), int(sys.argv[3]))
		
	elif sys.argv[1] == 'borrar':
		scraper  = Scraper_pubmed()
		scraper.borrar_abstracts()
	
	else:
		print "El orden de parametros es 1) descargar o borrar. En caso de seleccionar descargar: 2) Cantidad a descargar 3) cantidad de partes en las cuales dividir la descarga"
		
		
		
		
		
	

	
		








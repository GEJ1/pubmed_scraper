# -*- coding: utf-8 -*-

import subprocess
from time import time


def subproceso((inicio,fin)):
	todos = []
	
	for i in range(inicio,fin):
		p=subprocess.Popen(['python', 'correr_scraper_pubmed.py', str(i)])
		todos.append(p)

	exit_codes = [p.wait() for p in todos]
	

def dividir_input(total,paso):
	archivos = [] 	
	for x in range(1,total,paso):
		archivos.append((x,x+paso))
	return archivos
	
def procesar(cant_total, partes):
	
	archivos = dividir_input(cant_total,int(cant_total/partes))
	
	tiempo_inicial = time()
	
	for i in range(0, partes):
		
		subproceso(archivos[i])

	tiempo_final = time()
	
	
	tiempo_ejecucion = tiempo_final - tiempo_inicial
	
	print 'El tiempo de ejecucion fue:',tiempo_ejecucion , 'segundos'
	# Ej: El tiempo de ejecucion fue: 1639.53900003 para 10.000 papers

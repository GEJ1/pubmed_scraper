# coding=utf-8


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import Text
from nltk import FreqDist
from nltk.corpus import stopwords

import os
import re
import sys  
import string 


def ingrese_opcion():
	input_usuario = str(raw_input('Seleccione la opcion deseada y luego enter:  1- Grafico de dispersion  2- Grafico de frecuencia  3-Salir\n'))
	
	return resolver_menu(input_usuario)
	
def resolver_menu(input_usario):
    
    if input_usario == '2':
        
        fdist1 = FreqDist(filtered_words)
        fdist1.plot(30,cumulative=False)
       
        ingrese_opcion()
        
        
    elif input_usario == '1':
	
		
		palabras_plot = str(raw_input('Ingrese todas las palabras que desee separadas por un espacio y al finalizar presione enter:\n'))
		
		tokens_input = word_tokenize(palabras_plot)
		
		for palabra in tokens_input:
			
			palabras_clave.append(palabra)
			
		
		textList = Text(filtered_words)
		textList.dispersion_plot(palabras_clave)
		
		del palabras_clave[:] #Elimino todos los elementos de la lista por si uno quiere hacer otro grafico con palabras distintas
		
		ingrese_opcion()
		
    elif input_usario == '3':
		
		print 'presione cualquier tecla para cerrar la ventana'
		exit()
		
    else:
        print 'Seleccione 1,2 o 3'
        ingrese_opcion()
		


if __name__== '__main__':
	
	reload(sys)  
	sys.setdefaultencoding('utf8') #Necesario para el encoding

	text = open(os.path.join(os.getcwd(), 'Abstracts' , 'Todos_los_abstracts.txt'),'r').read()

	#Tokeniza el texto
	tokens = word_tokenize(text)
	
	#filtro las stopwords
	filtered_words = [w for w in tokens if not w in stopwords.words('english')]
	
	#Creo la lista que contendra a las palabras del grafico de dispersion
	palabras_clave = []
	
	ingrese_opcion()
	resolver_menu(opcion)
	

	
	




    

   

   


	


from sys import *
setrecursionlimit(1000000)

INPUT,I = stdin.buffer.read(),0


PUNTA, RAYA = ord('>'),ord('|')
def has_next(): return I < len(INPUT)

def leerflecha():
	global INPUT,I
	ans = 0
	if INPUT[I]!= PUNTA:
		ans +=1
		I+=2
	return ans
def leerinfo():
	global INPUT,I




def next_token():
	global INPUT,I
	pos_tree = leerflecha()
	

def main():
	for x in INPUT:
		print(x)

main()











"""AQUI DEBE IR LA CLASE ARBOL {indent_arrow}{body}[{author}|{ups}|{downs}|{comment_id}|{date}]"""
#class Ftree(object):
                 #Que atributos poner¿?
""" AQUI VOY A HACER EL PARSING ¿AL LEER UNA LINEA LLAMAR RECURSIVAMENTE HASTA ENCONTRAR LA HOJA?  """
"""
def parseline():
	line = stdin.readline().strip()
	pre = list()
	while len(line)!=0:
		read_line(line,pre)
		parseline()
	print(pre)

def read_line(line,lista):
	global n
	token = lista[0]
	i = 0
	cnt = 0
	while token !='>':		#Aqui estoy calculando la profundidad del nodo en el arbol
		i+=1
		token = lista[cnt+2]
	#Ahora debo leer al reves
	n = len(line)-2 #Aqui consumo el parentesis, digamos que me lo salto
	token1 = lista[n]
	date,comment_id,downs,ups, downs, author,body = None, None, None, None, None, None, None	
	while token1 !=	RCORCHETE:
		#token1 = lista[n]
		date = []
		while token1 != LINE:
			date.append(token1)			
			n = n-1
			token1 = lista[n]
"""


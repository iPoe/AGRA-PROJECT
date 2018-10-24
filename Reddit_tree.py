from sys import *
setrecursionlimit(1000000)

INPUT,I = stdin.buffer.read(),0


PUNTA, RAYA , LLAVEIZQ = ord('>'),ord('|'),ord('[')
def has_next(): return I < len(INPUT)

def leerflecha():
	global INPUT,I
	ans = 0
	while INPUT[I]!= PUNTA:
		ans +=1
		I+=2
	I+=1

	return ans
def leerinfo(id):
	global INPUT,I
	ans = None
	if id == 1:
		ans = []
		while INPUT[I]!= LLAVEIZQ and has_next():
			ans.append(chr(INPUT[I]))
			I+=1
		I+=1
		return ans

	elif id == 0:
		ans = 0
		while INPUT[I]!= RAYA and has_next():
			ans,I = int(chr(INPUT[I]))+ans*10,I+1
			
		I+=1
		return ans

	else:
		ans = []
		while INPUT[I]!= RAYA and has_next():
			ans.append(chr(INPUT[I]))
			I+=1
		I+=1
		return ans


def next_token():
	global INPUT,I
	pos_tree = leerflecha()
	body = leerinfo(1)
	author = leerinfo(2)
	ups = leerinfo(0)
	print(pos_tree)
	print(body)
	print(author)
	print(ups)
	return 0
	

def main():
	a = next_token()
	

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


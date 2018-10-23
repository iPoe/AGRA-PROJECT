from sys import stdin


PUNTA,RCORCHETE,LCORCHETE,SPACE,LINE = '>','[',']',' ','|'

"""AQUI DEBE IR LA CLASE ARBOL {indent_arrow}{body}[{author}|{ups}|{downs}|{comment_id}|{date}]"""
#class Ftree(object):
                 #Que atributos poner¿?
""" AQUI VOY A HACER EL PARSING ¿AL LEER UNA LINEA LLAMAR RECURSIVAMENTE HASTA ENCONTRAR LA HOJA?  """

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
	n = len(line)-1
	token1 = lista[-1]
	date,comment_id,downs,ups, downs, author,body = None, None, None, None, None, None, None	
	while token1 !=	RCORCHETE:
		token1 = lista[n-1]
		if token1 != LINE:









def main():
	#Leer las lineas
	parseline()



main()
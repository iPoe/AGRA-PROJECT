from sys import stdin
class Tree(object):
	def __init__(self,data,A,up,down):
		self.__len=len(A)
		self.__tree = A
		self.__data=data
		self.__likes=up
		self.__dislikes=down
		self.__Tlikes=up
		self.__Tdislikes=down
	def contarlikes(self):
		if self.__len==0:
			return (self.__Tlikes,self.__Tdislikes)
		else:
			likes,dislikes=self.__likes,self.__dislikes
			for i in self.__tree:
				S=i.contarlikes(); likes+=S[0] ; dislikes+=S[1]
		self.__Tlikes,self.__Tdislikes=likes,dislikes	
		return (likes,dislikes)
	def imprimir(self):
		print(self.__Tlikes,self.__Tdislikes)		
		for i in self.__tree:
			i.imprimir()
def parse_line():
	global line
	tkn = None; i = 2 #leo ']'
	while tkn != '[': 
		tkn = line[-1*i]
		i += 1
	low, hi = len(line) - i + 2, len(line)-1
	nombre, ups, dwns, id, date = line[low:hi].split('|')
	while tkn != '>': 
		tkn = line[-1*i]
		i += 1
	low, hi = len(line) - i + 2, low - 1
	body = line[low:hi]
	while i < len(line): i += 1
	prof = low//2
	return (prof, body, nombre, ups, dwns, id, date)
I=0
def create():
	global I
	Arbol=None
	if I<len(PREORDER):
			j=I			
			childs=[]	#Esta condición es suficiente para que cuando tengan depths == se crea otro hijo		
			while I+1<len(PREORDER) and PREORDER[j][0]!=PREORDER[I+1][0]:
				I+=1
				if PREORDER[j][0]+1== PREORDER[I][0]:					
					t=create()
					if t!= None:
						childs.append(t)
			I=j

			Arbol=Tree(PREORDER[j][1],childs,PREORDER[j][2],PREORDER[j][3])		
						
	return Arbol

def main():
	global line, PREORDER
	line = stdin.readline().strip()
	PREORDER = list() # suponiendo un foro	
	while(len(line) != 0):
		prof, body, nombre, ups, dwns, id, date = parse_line() #cada vez que haya una profundidad 0 debo reiniciar el preorden y el arbol
		PREORDER.append((int(prof),id,int(ups),int(dwns)))		
		line = stdin.readline().strip()
		"""
		if authors.get('nombre')!=None:
			authors['nombre']=1
		else:
			authors['nombre']+=1
		"""

	Arbol=create()
	
	Arbol.contarlikes()
	for id in PREORDER[:len(PREORDER)-1]:
		print(id[1], end = ' ')
	print(PREORDER[-1])

	Arbol.imprimir()
	

main()




from sys import stdin
class Tree(object):
	def __init__(self,data,A=[]):
		self.__len=len(A)
		self.__tree = A
		self.__data=data
		self.__likes=0
		self.__dislikes=0
	def contarlikes(self):
		if self.__len(self.__tree)==0:
			return (self.__likes,self.__dislikes)
		else:
			likes,dislikes=self.__likes,self.__dislikes
			for i in __tree:
				S=i.contarlikes()
				likes+=S[0]
				dislikes+=S[1]
		return (likes,dislikes)
	def imprimir(self):
		print(self.__data)		
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
def create(d):
	global I
	Arbol=None
	while I<len(PREORDER):
			j=I
			childs=[]			
			while I<len(PREORDER) and d+1== PREORDER[I][0]:
				I+=1
				t=create(d+1)
				if t!= None:
					childs.append(t)				
			I+=1
			Arbol=Tree(PREORDER[j][1],childs)
			
	return Arbol

def main():
	global line, PREORDER
	line = stdin.readline().strip()
	PREORDER = list() # suponiendo un foro
	while(len(line) != 0):
		prof, body, nombre, ups, dwns, id, date = parse_line() #cada vez que haya una profundidad 0 debo reiniciar el preorden y el arbol
		PREORDER.append((prof,id))

		
		line = stdin.readline().strip()

	Arbol=create(0)
	Arbol.imprimir()
	"""
	for id in PREORDER[:len(PREORDER)-1]:
		print(id, end = ' ')
	print(PREORDER[-1])
	"""
main()




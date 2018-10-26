from sys import stdin
D=[]
class Tree(object):
	def __init__(self,data,up,down):
		self.__len=0
		self.__tree = []
		self.__data=data
		self.__likes=up
		self.__dislikes=down
		self.Tlikes=up
		self.Tdislikes=down
	def newChild(self,T):
		self.__tree.append(T)
		self.__len+=1
	def contarlikes(self):
		if self.__len==0:
			return (self.Tlikes,self.Tdislikes)
		else:
			likes,dislikes=self.__likes,self.__dislikes
			for i in self.__tree:
				if i!= None:
					S=i.contarlikes(); likes+=S[0] ; dislikes+=S[1]
		self.Tlikes,self.Tdislikes=likes,dislikes	
		return (likes,dislikes)
	def getTree(self):
		return self.__tree
	def __str__(self):
		#print(self.__Tlikes,self.__Tdislikes)
		S = self.__data		
		for i in self.__tree:
			S += ' ' +  str(i)
		return S
	def imprimir(self):		
		print(self.Tlikes,self.Tdislikes)		
		for i in self.__tree:
			if i != None:
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
def create(prof,u,d,i):
	global PREORDER,line	
	line = stdin.readline().strip()
	ARBOL=Tree(i,u,d)
	if len(line)!=0:
		nextprof,body, nombre, ups, dwns, id, date = parse_line() 
		PREORDER.append(id)
		
		while(len(line)!=0 and int(prof)+1<=int(nextprof)):

			
			ARBOL.newChild(create(prof+1,int(ups),int(dwns),id))
		

			

	return ARBOL

def main():
	global line, PREORDER,D
	line = stdin.readline().strip()
	PREORDER = list() # suponiendo un foro
	#authors = {}	
	prof, body, nombre, ups, dwns, id, date = parse_line() #cada vez que haya una profundidad 0 debo reiniciar el preorden y el arbol
	PREORDER.append(id)

	Arbol = create(prof,int(ups),int(dwns),id)
	print(len(Arbol.getTree()))
	#Arbol.contarlikes()
	"""	
	if authors.get(nombre)==None:
		authors[nombre]=1
	else:
		authors[nombre]+=1
	"""

	

	
	
	#for id in PREORDER[:len(PREORDER)-1]:
	#	print(id, end = ' ')
	#print(PREORDER[-1])
	print(Arbol)
	print(Arbol.getTree())
		 
	#Arbol.imprimir()
	#s = sorted(authors.items(),key=lambda x: x[0])	
	#for key,value in sorted(s,key=lambda x:x[1],reverse=True):
		#print(key,value)
	

main()

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
		if len(self.__tree)==0:
			return (self.__Tlikes,self.__Tdislikes)
		else:
			likes,dislikes=self.__likes,self.__dislikes
			for i in self.__tree:
				S=i.contarlikes()
				likes+=S[0]
				dislikes+=S[1]
		self.__Tlikes=likes
		self.__Tdislikes = dislikes
		return (likes,dislikes)
	def __str__(self):
		#print(self.__Tlikes,self.__Tdislikes)
		S = self.__data		
		for i in self.__tree:
			S += ' ' +  str(i)
		return S
	def __len__(self):
		return self.__len
	def newChild(self,T):
		self.__tree.append(T)
		self.__len+=1
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
	Arbol=Tree(PREORDER[I][1],list(),PREORDER[I][2],PREORDER[I][3])
	if I<len(PREORDER):
			j=I			
			childs=[]	#Esta condición es suficiente para que cuando tengan depths == se crea otro hijo		
			while I+1<len(PREORDER) and PREORDER[j][0]!=PREORDER[I+1][0]:
				I+=1
				if PREORDER[j][0]+1== PREORDER[I][0]:					
					
					
					Arbol.newChild(create())
				
			I=j
								
	return Arbol

def main():
	global line, PREORDER,I
	
	line = stdin.readline().strip()
	if len(line) != 0: prof, body, nombre, ups, dwns, id, date = parse_line()

	while(len(line)!=0):
		PREORDER = list() # suponiendo un foro, que pasa cuando hay varios foros, hay que limpiarlo
		authors = {}		
		ok = True
		while(ok and len(line)!= 0):		
			PREORDER.append((int(prof),id,int(ups),int(dwns)))		
							
			if authors.get(nombre)==None:
				authors[nombre]=1
			else:
				authors[nombre]+=1
			line = stdin.readline().strip()
			if len(line)!= 0:
				prof, body, nombre, ups, dwns, id, date = parse_line()
				if prof == 0:
					ok = False
					I = 0
		#print(PREORDER)
		Arbol=create()	
		print(len(Arbol))
		Arbol.contarlikes()
		#for id in PREORDER[:len(PREORDER)-1]:
		#	print(id[1], end = ' ')
		#print(PREORDER[-1][1])
		print(Arbol)
		Arbol.imprimir()
		s = sorted(authors.items(),key=lambda x: x[0])	
		for key,value in sorted(s,key=lambda x:x[1],reverse=True):
			print(key,value)
		

main()
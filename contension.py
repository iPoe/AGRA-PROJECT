class Tree(object):
	def __init__(self,data,A,up,down):
		self.__len=len(A)
		self.__tree = A
		self.__data=data
		self.__likes=up
		self.__dislikes=down
		self.__Tlikes=up
		self.__Tdislikes=down
	def imprimir(self):
		#print(self.__Tlikes,self.__Tdislikes)
		print(self.__data,end=' ')		
		for i in self.__tree:
			i.imprimir()
I = 0	
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
PREORDER = [(0, '9lbbff', 41667, 0), (1, 'e75fqb9', 1177, 0), (2, 'e75j9er', 478, 0), (3, 'e75n5cg', 165, 0), (4, 'e75t519', 55, 0), (5, 'e75xytg', 10, 0), (4, 'e75qy5i', 8, 0), (4, 'e75yvqc', 1, 0), (3, 'e75onm1', 19, 0), (3, 'e76abvm', 1, 0), (2, 'e75nupx', 9, 0), (2, 'e75qiog', 4, 0), (2, 'e76111l', 3, 0), (2, 'e75reyc', 3, 0), (1, 'e75e753', 389, 0), (2, 'e75ebup', 423, 0), (3, 'e75n1s3', 78, 0), (4, 'e75ofpw', 30, 0), (4, 'e75txsh', 15, 0), (5, 'e76jqqu', 1, 0), (4, 'e76cist', 6, 0), (3, 'e75p73l', 24, 0), (2, 'e7679x7', 3, 0), (1, 'e75d29c', 427, 0), (2, 'e75fzeq', 121, 0), (3, 'e75hig4', 125, 0), (4, 'e75ii94', 75, 0), (5, 'e7664q7', 4, 0), (5, 'e75iol6', 33, 0), (5, 'e75zecz', 17, 0), (5, 'e76ce3z', 4, 0), (4, 'e75n5yz', 4, 0), (4, 'e75y41v', 3, 0), (4, 'e75lnhq', 5, 0), (4, 'e76nxwn', 1, 0), (4, 'e75lswc', 0, 0), (5, 'e75uhvc', 6, 0), (5, 'e75y218', 3, 0), (2, 'e75i0up', 10, 0), (3, 'e75n8ru', 3, 0), (2, 'e75lmd8', 4, 0), (2, 'e75w8xu', 3, 0), (2, 'e75hkx8', 5, 0), (3, 'e75k2b0', 10, 0), (1, 'e75km7x', 92, 0), (2, 'e76b0py', 16, 0), (3, 'e76hw7g', 3, 0), (4, 'e76texs', 1, 0), (1, 'e75h5tz', 57, 0), (1, 'e75jmxo', 47, 0), (1, 'e75gj1m', 64, 0), (2, 'e75o8b8', 7, 0), (3, 'e75r96r', 3, 0), (4, 'e75ww8e', 4, 0), (1, 'e75eif4', 40, 0), (2, 'e75ki8n', 35, 0), (3, 'e75nbhx', 16, 0), (4, 'e765y66', 1, 0), (5, 'e76f6ok', 2, 0), (2, 'e75gyfk', 12, 0), (2, 'e75ip2p', 13, 0), (1, 'e75kbr1', 38, 0), (1, 'e75boil', 18, 0), (1, 'e75hpw6', 7, 0), (1, 'e75lf9x', 6, 0), (1, 'e75m6yp', 6, 0), (1, 'e75obkj', 6, 0), (1, 'e75k1wk', 6, 0), (1, 'e75ktrv', 6, 0), (3, 'e75ku9t', 6, 0), (3, 'e75lfld', 3, 0), (1, 'e75m4hr', 5, 0), (1, 'e75gtex', 5, 0), (1, 'e75od46', 5, 0), (1, 'e75kxg8', 3, 0), (1, 'e75gqy8', 2, 0), (1, 'e75hv1q', 2, 0), (2, 'e75ncwt', 1, 0), (1, 'e75ih8e', 2, 0), (1, 'e75iyod', 2, 0), (1, 'e75jzw4', 2, 0), (1, 'e75kf15', 2, 0), (1, 'e75kq2p', 2, 0), (1, 'e75mi32', 2, 0), (1, 'e75neph', 2, 0), (1, 'e75nnvr', 2, 0), (1, 'e75qgi5', 2, 0), (1, 'e75uhtp', 2, 0), (1, 'e76sgb4', 2, 0), (1, 'e75kue9', 4, 0), (1, 'e75jlgw', 1, 0), (1, 'e75jovj', 1, 0), (1, 'e75js4t', 1, 0), (1, 'e75jy33', 1, 0), (1, 'e75k8z4', 1, 0), (1, 'e75l4ny', 1, 0), (1, 'e75lpxr', 1, 0), (1, 'e75mvnk', 1, 0), (1, 'e75o0rn', 1, 0), (1, 'e75okdq', 1, 0), (1, 'e75otxg', 1, 0), (1, 'e75ovvv', 1, 0), (1, 'e75pkyh', 1, 0), (1, 'e75q02d', 1, 0), (1, 'e75qeja', 1, 0), (3, 'e75qerb', 2, 0), (1, 'e75qm74', 1, 0), (1, 'e75qzs5', 1, 0), (1, 'e75r96g', 1, 0), (1, 'e75rbcf', 1, 0), (1, 'e75rem6', 1, 0), (1, 'e75si0o', 1, 0), (1, 'e75t917', 1, 0), (1, 'e75vbgq', 1, 0), (1, 'e75vtld', 1, 0), (1, 'e75vvxa', 1, 0), (1, 'e75w1fy', 1, 0), (1, 'e75xnen', 1, 0), (1, 'e75xr8b', 1, 0), (1, 'e75y2xg', 1, 0), (1, 'e75z38t', 1, 0), (1, 'e75z3ja', 1, 0), (1, 'e75zike', 1, 0), (1, 'e75zydm', 1, 0), (1, 'e761372', 1, 0), (1, 'e7624zh', 1, 0), (1, 'e762lwm', 1, 0), (1, 'e762rgc', 1, 0), (1, 'e763jdo', 1, 0), (1, 'e767loh', 1, 0), (1, 'e768hev', 1, 0), (1, 'e7692oi', 1, 0), (1, 'e769eou', 1, 0), (1, 'e769l8u', 1, 0), (1, 'e76ar3m', 1, 0), (1, 'e76cewk', 1, 0), (1, 'e76ewtc', 1, 0), (1, 'e76ft95', 1, 0), (1, 'e76i6be', 1, 0), (1, 'e75rr6y', 1, 0), (1, 'e75jfpr', 0, 0), (2, 'e75uj3s', 2, 0), (3, 'e75wbyw', 1, 0), (1, 'e75m7fn', 0, 0), (1, 'e75ojvl', 0, 0), (1, 'e75vdvb', 0, 0)]

def main():
	Arbol = create()
	Arbol.imprimir()
main()

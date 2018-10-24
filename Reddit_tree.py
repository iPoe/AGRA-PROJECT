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




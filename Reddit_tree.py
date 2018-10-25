from sys import stdin
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

def main():
	global line, PREORDER
	line = stdin.readline().strip()
	PREORDER = list() # suponiendo un foro
	while(len(line) != 0):
		prof, body, nombre, ups, dwns, id, date = parse_line() #cada vez que haya una profundidad 0 debo reiniciar el preorden y el arbol
		PREORDER.append(id)
		
		line = stdin.readline().strip()
	
	for id in PREORDER[:len(PREORDER)-1]:
		print(id, end = ' ')
	print(PREORDER[-1])

main()




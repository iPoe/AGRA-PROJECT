

def main():
    linea = "2018-10-04 15:11:38"
    ans = []
    N = len(linea)    
    for i in range(N-1,-1,-1):
        ans.append(linea[i])
        #print(linea[i])

    l = ''.join(ans[::-1])
    print(l)
    print(linea)
    print(N)
    
main()        

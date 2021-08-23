import sys


e = 10**-16

if len(sys.argv) == 3:
    n = int(sys.argv[1])
    x = int(sys.argv[2])
else: print ("El número de argumentos es incompleto")    

def calcular (x,n):
    return (1/2*(x+(n/x)))


y = calcular (x,n)
while abs(x-y) > e:
    print ("Y = ",y)
    x = y
    y = calcular (x,n)
    

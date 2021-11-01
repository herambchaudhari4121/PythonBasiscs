# Programa en python para chequear si un numero es ganador

# Devuelve  1 si n es un numero ganador
# De lo contrario devuelve 0
def isLucky(n):
	

	
	if isLucky.counter > n:
		return 1
	if n % isLucky.counter == 0:
		return 0
	

	next_position = n - (n/isLucky.counter)
	
	isLucky.counter = isLucky.counter + 1
	
	return isLucky(next_position)
	
	


isLucky.counter = 2 
x = 5
if isLucky(x):
	print x,"Es un numero ganador"
else:
	print x,"No es un numero ganador"
	


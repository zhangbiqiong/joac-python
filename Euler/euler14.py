def calcularSecuencia(numero):
	contador = 0
	while numero > 1:
		if numero%2:
			numero = 3*numero + 1
		else:
			numero = numero/2
		contador += 1
	return contador

memoria = (0, 0)
for a in xrange(1000000, 1, -1):
	numero = calcularSecuencia(a)
	if numero > memoria[1]: memoria=(a, numero)
	
print memoria

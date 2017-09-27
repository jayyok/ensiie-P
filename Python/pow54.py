#!/usr/bin/python3

def elevatePow54(x):
	x3= x*x*x
	x9=x3*x3*x3
	x27=x9*x9*x9
	x54=x27*x27
	return x54


x = int(input())


print('x pre : ' + str(x))

# Appel de la fct
x = elevatePow54(x)

print('x post : ' + str(x))





	
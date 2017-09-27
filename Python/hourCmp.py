#!/usr/bin/python3

def timeCmp(h1,m1,s1,h2,m2,s2):
	h1Sec = h1 * 3600 + m1 * 60 + s1
	h2Sec = h2 * 3600 + m2 * 60 + s2
	diff = h2Sec - h1Sec
	if(diff>0):
		print('Resultat :' + str(int(diff/3600)) + ':' + str(int(diff%3600/60)) + ':' + str(int(diff%3600%60)) + ':')
	else:
		print('Resultat : - ' + str(int(diff/3600)) + ':' + str(int(diff%3600/60)) + ':' + str(int(diff%3600%60)) + ':')

h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

print('H1' + str(h1) + ':' + str(m1) + ':' + str(s1))

print('H2' + str(h2) + ':' + str(m2) + ':' + str(s2))

# Appel de la fct
timeCmp(h1,m1,s1,h2,m2,s2)



	